from faker import Faker
import random
import client
import traceback

fake = Faker()

def insertDummyData():
    try:
        # Insert HealthInstitution data
        InsertHealthInstitution = """    
            INSERT INTO HealthInstitution (
                HealthInstitutionName,
                HealthInstitutionDesc,
                HealthInstitutionEmailAddress,
                HealthInstitutionOpenTime,
                HealthInstitutionCloseTime,
                HealthInstitutionType,
                HealthInstitutionAddress,
                HealthInstitutionAddressLong,
                HealthInstitutionAddressLat,
                created_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            ON CONFLICT (HealthInstitutionName) 
            DO UPDATE SET
                HealthInstitutionDesc = EXCLUDED.HealthInstitutionDesc,
                HealthInstitutionEmailAddress = EXCLUDED.HealthInstitutionEmailAddress,
                HealthInstitutionOpenTime = EXCLUDED.HealthInstitutionOpenTime,
                HealthInstitutionCloseTime = EXCLUDED.HealthInstitutionCloseTime,
                HealthInstitutionType = EXCLUDED.HealthInstitutionType,
                HealthInstitutionAddress = EXCLUDED.HealthInstitutionAddress,
                HealthInstitutionAddressLong = EXCLUDED.HealthInstitutionAddressLong,
                HealthInstitutionAddressLat = EXCLUDED.HealthInstitutionAddressLat,
                updated_at = NOW();
        """
        
        print("Generating ddata for HealthInstitution...")
        healthInstitutionData = []
        for _ in range(10):
            healthInstitutionData.append({
                "HealthInstitutionName": fake.company(),
                "HealthInstitutionDesc": fake.catch_phrase(),
                "HealthInstitutionEmailAddress": fake.email(),
                "HealthInstitutionOpenTime": fake.time(),
                "HealthInstitutionCloseTime": fake.time(),
                "HealthInstitutionType": random.choice(['Hospital', 'Clinic', 'Pharmacy']),
                "HealthInstitutionAddress": fake.address(),
                "HealthInstitutionAddressLong": fake.longitude(),
                "HealthInstitutionAddressLat": fake.latitude()
            })
         
        print("Adding ddata to HealthInstitution...")
        for healthInstitutionContent in healthInstitutionData:
            try:
                client.cursor.execute(InsertHealthInstitution, (
                    healthInstitutionContent["HealthInstitutionName"],
                    healthInstitutionContent["HealthInstitutionDesc"],
                    healthInstitutionContent["HealthInstitutionEmailAddress"],
                    healthInstitutionContent["HealthInstitutionOpenTime"],
                    healthInstitutionContent["HealthInstitutionCloseTime"],
                    healthInstitutionContent["HealthInstitutionType"],
                    healthInstitutionContent["HealthInstitutionAddress"],
                    healthInstitutionContent["HealthInstitutionAddressLong"],
                    healthInstitutionContent["HealthInstitutionAddressLat"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in HealthInstitution table while inserting: {healthInstitutionContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        # Insert HealthInstitutionService data
        InsertHealthInstitutionService = """    
            INSERT INTO HealthInstitutionService (
                HealthInstitutionServiceName,
                HealthInstitutionServiceDesc,
                HealthInstitutionID,
                created_at
            ) VALUES (%s, %s, %s, NOW())
            ON CONFLICT (HealthInstitutionServiceID) 
            DO UPDATE SET
                HealthInstitutionServiceDesc = EXCLUDED.HealthInstitutionServiceDesc,
                updated_at = NOW();
        """
        
        print("Fetching HealthInstitutionIDs to assign...")
        fetchAllHealthIntitutionID = "SELECT HealthInstitutionID FROM HealthInstitution;"
        client.cursor.execute(fetchAllHealthIntitutionID)
        allHealthInstitutionIdData = [row[0] for row in client.cursor.fetchall()]
        
        print("Generating ddata for HealthInstitutionService...")
        healthInstitutionServiceData = []
        for healthInstitutionContentForService in allHealthInstitutionIdData:
            healthInstitutionServiceData.append({
                "HealthInstitutionServiceName": fake.bs(),
                "HealthInstitutionServiceDesc": fake.sentence(),
                "HealthInstitutionID": healthInstitutionContentForService
            })
        
        print("Adding ddata to HealthInstitutionService...")
        for healthInstitutionServiceContent in healthInstitutionServiceData:
            try:
                client.cursor.execute(InsertHealthInstitutionService, (
                    healthInstitutionServiceContent["HealthInstitutionServiceName"],
                    healthInstitutionServiceContent["HealthInstitutionServiceDesc"],
                    healthInstitutionServiceContent["HealthInstitutionID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in HealthInstitutionService table while inserting: {healthInstitutionServiceContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        # Insert HealthInstitutionAcreditedInsurance data
        InsertHealthInstitutionAcreditedInsurance = """    
            INSERT INTO HealthInstitutionAcreditedInsurance (
                HealthInstitutionAcreditedInsuranceName,
                HealthInstitutionAcreditedInsuranceDesc,
                HealthInstitutionID,
                created_at
            ) VALUES (%s, %s, %s, NOW())
            ON CONFLICT (HealthInstitutionAcreditedInsuranceID) 
            DO UPDATE SET
                HealthInstitutionAcreditedInsuranceDesc = EXCLUDED.HealthInstitutionAcreditedInsuranceDesc,
                updated_at = NOW();
        """

        print("Generating ddata for HealthInstitutionAcreditedInsurance...")        
        healthInstitutionAcreditedInsuranceData = []
        for healthInstitutionContentForInsurance in allHealthInstitutionIdData:
            healthInstitutionAcreditedInsuranceData.append({
                "HealthInstitutionAcreditedInsuranceName": fake.company(),
                "HealthInstitutionAcreditedInsuranceDesc": fake.catch_phrase(),
                "HealthInstitutionID": healthInstitutionContentForInsurance
            })

        print("Adding ddata to HealthInstitutionAcreditedInsurance...")
        for healthInstitutionAcceptedInsuranceContent in healthInstitutionAcreditedInsuranceData:
            try:
                client.cursor.execute(InsertHealthInstitutionAcreditedInsurance, (
                    healthInstitutionAcceptedInsuranceContent["HealthInstitutionAcreditedInsuranceName"],
                    healthInstitutionAcceptedInsuranceContent["HealthInstitutionAcreditedInsuranceDesc"],
                    healthInstitutionAcceptedInsuranceContent["HealthInstitutionID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in HealthInstitutionAcreditedInsurance table while inserting: {healthInstitutionAcceptedInsuranceContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        # Insert FinancialInstitution data
        InsertFinancialInstitution = """    
            INSERT INTO FinancialInstitution (
                FinancialInstitutionName,
                FinancialInstitutionDesc,
                FinancialInstitutionEmailAddress,
                FinancialInstitutionOpenTime,
                FinancialInstitutionCloseTime,
                FinancialInstitutionType,
                FinancialInstitutionAddress,
                FinancialInstitutionAddressLong,
                FinancialInstitutionAddressLat,
                created_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            ON CONFLICT (FinancialInstitutionName) 
            DO UPDATE SET
                FinancialInstitutionDesc = EXCLUDED.FinancialInstitutionDesc,
                FinancialInstitutionEmailAddress = EXCLUDED.FinancialInstitutionEmailAddress,
                FinancialInstitutionOpenTime = EXCLUDED.FinancialInstitutionOpenTime,
                FinancialInstitutionCloseTime = EXCLUDED.FinancialInstitutionCloseTime,
                FinancialInstitutionType = EXCLUDED.FinancialInstitutionType,
                FinancialInstitutionAddress = EXCLUDED.FinancialInstitutionAddress,
                FinancialInstitutionAddressLong = EXCLUDED.FinancialInstitutionAddressLong,
                FinancialInstitutionAddressLat = EXCLUDED.FinancialInstitutionAddressLat,
                updated_at = NOW();
        """
        
        print("Generating ddata for FinancialInstitution...")        
        financialInstitutionData = []
        for _ in range(5):
            financialInstitutionData.append({
                "FinancialInstitutionName": fake.company(),
                "FinancialInstitutionDesc": fake.bs(),
                "FinancialInstitutionEmailAddress": fake.email(),
                "FinancialInstitutionOpenTime": fake.time(),
                "FinancialInstitutionCloseTime": fake.time(),
                "FinancialInstitutionType": random.choice(['Bank', 'Insurance', 'Investment']),
                "FinancialInstitutionAddress": fake.address(),
                "FinancialInstitutionAddressLong": fake.longitude(),
                "FinancialInstitutionAddressLat": fake.latitude()
            })

        print("Adding ddata to FinancialInstitution...")
        for financialInstitutionContent in financialInstitutionData:
            try:
                client.cursor.execute(InsertFinancialInstitution, (
                    financialInstitutionContent["FinancialInstitutionName"],
                    financialInstitutionContent["FinancialInstitutionDesc"],
                    financialInstitutionContent["FinancialInstitutionEmailAddress"],
                    financialInstitutionContent["FinancialInstitutionOpenTime"],
                    financialInstitutionContent["FinancialInstitutionCloseTime"],
                    financialInstitutionContent["FinancialInstitutionType"],
                    financialInstitutionContent["FinancialInstitutionAddress"],
                    financialInstitutionContent["FinancialInstitutionAddressLong"],
                    financialInstitutionContent["FinancialInstitutionAddressLat"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in FinancialInstitution table while inserting: {financialInstitutionContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        # Insert FinancialInstitutionNote data
        InsertFinancialInstitutionNote = """    
            INSERT INTO FinancialInstitutionNote (
                FinancialInstitutionNoteName,
                FinancialInstitutionNoteDesc,
                FinancialInstitutionID,
                created_at
            ) VALUES (%s, %s, %s, NOW())
            ON CONFLICT (FinancialInstitutionNoteID) 
            DO UPDATE SET
                FinancialInstitutionNoteDesc = EXCLUDED.FinancialInstitutionNoteDesc,
                updated_at = NOW();
        """

        print("Fetching FinancialInstitutionIDs to assign...")
        fetchAllFinancialIntitutionID = "SELECT FinancialInstitutionID FROM FinancialInstitution;"
        client.cursor.execute(fetchAllFinancialIntitutionID)
        fetchAllFinancialIntitutionID = [row[0] for row in client.cursor.fetchall()]
        
        print("Generating ddata for FinancialInstitutionNote...")        
        financialInstitutionNoteData = []
        for financialInstitutionContentForNote in fetchAllFinancialIntitutionID:
            financialInstitutionNoteData.append({
                "FinancialInstitutionNoteName": fake.bs(),
                "FinancialInstitutionNoteDesc": fake.sentence(),
                "FinancialInstitutionID": financialInstitutionContentForNote
            })

        print("Adding ddata to FinancialInstitutionNote...")
        for financialInstitutionNoteContent in financialInstitutionNoteData:
            try:
                client.cursor.execute(InsertFinancialInstitutionNote, (
                    financialInstitutionNoteContent["FinancialInstitutionNoteName"],
                    financialInstitutionNoteContent["FinancialInstitutionNoteDesc"],
                    financialInstitutionNoteContent["FinancialInstitutionID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in FinancialInstitutionNote table while inserting: {financialInstitutionNoteContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        # Insert FinancialInstitutionBenefit data
        InsertFinancialInstitutionBenefit = """    
            INSERT INTO FinancialInstitutionBenefit (
                FinancialInstitutionBenefitName,
                FinancialInstitutionBenefitDesc,
                FinancialInstitutionID,
                created_at
            ) VALUES (%s, %s, %s, NOW())
            ON CONFLICT (FinancialInstitutionBenefitID) 
            DO UPDATE SET
                FinancialInstitutionBenefitDesc = EXCLUDED.FinancialInstitutionBenefitDesc,
                updated_at = NOW();
        """

        print("Generating ddata for FinancialInstitutionBenefit...")        
        financialInstitutionBenefitData = []
        for financialInstitutionContentForBenefit in fetchAllFinancialIntitutionID:
            financialInstitutionBenefitData.append({
                "FinancialInstitutionBenefitName": fake.bs(),
                "FinancialInstitutionBenefitDesc": fake.sentence(),
                "FinancialInstitutionID": financialInstitutionContentForBenefit
            })

        print("Adding ddata to FinancialInstitutionBenefit...")
        for financialInstitutionBenefitContent in financialInstitutionBenefitData:
            try:
                client.cursor.execute(InsertFinancialInstitutionBenefit, (
                    financialInstitutionBenefitContent["FinancialInstitutionBenefitName"],
                    financialInstitutionBenefitContent["FinancialInstitutionBenefitDesc"],
                    financialInstitutionBenefitContent["FinancialInstitutionID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in FinancialInstitutionBenefit table while inserting: {financialInstitutionBenefitContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        # Insert FinancialInstitutionProcess data
        InsertFinancialInstitutionProcess = """    
            INSERT INTO FinancialInstitutionProcess (
                FinancialInstitutionProcessDesc,
                FinancialInstitutionBenefitID,
                created_at
            ) VALUES (%s, %s, NOW())
            ON CONFLICT (FinancialInstitutionProcessID) 
            DO UPDATE SET
                updated_at = NOW();
        """

        print("Fetching FinancialInstitutionBenefitID to assign...")
        fetchAllFinancialIntitutionBenefitID = "SELECT FinancialInstitutionBenefitID FROM FinancialInstitutionBenefit;"
        client.cursor.execute(fetchAllFinancialIntitutionBenefitID)
        fetchAllFinancialIntitutionBenefitID = [row[0] for row in client.cursor.fetchall()]

        print("Generating ddata for FinancialInstitutionProcess...")        
        financialInstitutionProcessData = []
        for financialInstitutionBenefitContentForProcess in fetchAllFinancialIntitutionBenefitID:
            financialInstitutionProcessData.append({
                "FinancialInstitutionProcessDesc": fake.sentence(),
                "FinancialInstitutionBenefitID": financialInstitutionBenefitContentForProcess
            })

        print("Adding ddata to FinancialInstitutionProcess...")
        for financialInstitutionProcessContent in financialInstitutionProcessData:
            try:
                client.cursor.execute(InsertFinancialInstitutionProcess, (
                    financialInstitutionProcessContent["FinancialInstitutionProcessDesc"],
                    financialInstitutionProcessContent["FinancialInstitutionBenefitID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in FinancialInstitutionProcess table while inserting: {financialInstitutionProcessContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        # Insert BenefitInclusion data
        InsertBenefitInclusion = """    
            INSERT INTO BenefitInclusion (
                BenefitInclusionTitle,
                BenefitInclusionDesc,
                FinancialInstitutionBenefitID,
                created_at
            ) VALUES (%s, %s, %s, NOW())
            ON CONFLICT (BenefitInclusionID) 
            DO UPDATE SET
                BenefitInclusionDesc = EXCLUDED.BenefitInclusionDesc,
                updated_at = NOW();
        """

        print("Generating ddata for BenefitInclusion...")        
        BenefitInclusionData = []
        for financialInstitutionBenefitContentForList in fetchAllFinancialIntitutionBenefitID:
            BenefitInclusionData.append({
                "BenefitInclusionTitle": fake.bs(),
                "BenefitInclusionDesc": fake.sentence(),
                "FinancialInstitutionBenefitID": financialInstitutionBenefitContentForList
            })

        print("Adding ddata to BenefitInclusion...")
        for BenefitInclusionContent in BenefitInclusionData:
            try:
                client.cursor.execute(InsertBenefitInclusion, (
                    BenefitInclusionContent["BenefitInclusionTitle"],
                    BenefitInclusionContent["BenefitInclusionDesc"],
                    BenefitInclusionContent["FinancialInstitutionBenefitID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in BenefitInclusion table while inserting: {BenefitInclusionContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        # Insert FinancialInstitutionRequirement data
        InsertFinancialInstitutionRequirement = """    
            INSERT INTO FinancialInstitutionRequirement (
                FinancialInstitutionRequirementName,
                FinancialInstitutionRequirementDesc,
                FinancialInstitutionRequirementType,
                FinancialInstitutionBenefitID,
                created_at
            ) VALUES (%s, %s, %s, %s, NOW())
            ON CONFLICT (FinancialInstitutionRequirementID) 
            DO UPDATE SET
                FinancialInstitutionRequirementDesc = EXCLUDED.FinancialInstitutionRequirementDesc,
                FinancialInstitutionRequirementType = EXCLUDED.FinancialInstitutionRequirementType,
                updated_at = NOW();
        """

        print("Generating ddata for FinancialInstitutionRequirement...")        
        financialInstitutionRequirementData = []
        for financialInstitutionBenefitContentForRequirement in fetchAllFinancialIntitutionBenefitID:
            financialInstitutionRequirementData.append({
                "FinancialInstitutionRequirementName": fake.bs(),
                "FinancialInstitutionRequirementDesc": fake.sentence(),
                "FinancialInstitutionRequirementType": random.choice(['Document', 'Action']),
                "FinancialInstitutionBenefitID": financialInstitutionBenefitContentForRequirement
            })

        print("Adding ddata to FinancialInstitutionRequirement...")
        for financialInstitutionRequirementContent in financialInstitutionRequirementData:
            try:
                client.cursor.execute(InsertFinancialInstitutionRequirement, (
                    financialInstitutionRequirementContent["FinancialInstitutionRequirementName"],
                    financialInstitutionRequirementContent["FinancialInstitutionRequirementDesc"],
                    financialInstitutionRequirementContent["FinancialInstitutionRequirementType"],
                    financialInstitutionRequirementContent["FinancialInstitutionBenefitID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in FinancialInstitutionRequirement table while inserting: {financialInstitutionRequirementContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()
        
        # Insert Blog data
        InsertBlog = """    
            INSERT INTO Blog (
                BlogName,
                BlogAuthor,
                created_at
            ) VALUES (%s, %s, NOW())
            ON CONFLICT (BlogID) 
            DO UPDATE SET
                BlogAuthor = EXCLUDED.BlogAuthor,
                updated_at = NOW();
        """
        
        print("Generating ddata for Blog...")        
        blogData = []
        for _ in range(5):
            blogData.append({
                "BlogName": fake.bs(),
                "BlogAuthor": fake.name()
            })

        print("Adding ddata to Blog...")
        for blogContent in blogData:
            try:
                client.cursor.execute(InsertBlog, (
                    blogContent["BlogName"],
                    blogContent["BlogAuthor"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in Blog table while inserting: {blogContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()
        
        # Insert BlogRefLink data
        InsertBlogRefLink = """    
            INSERT INTO BlogRefLink (
                BlogRefLink,
                BlogID,
                created_at
            ) VALUES (%s, %s, NOW())
            ON CONFLICT (BlogRefLinkID) 
            DO UPDATE SET
                updated_at = NOW();
        """
        
        print("Fetching BlogID to assign...")
        fetchAllBlogID = "SELECT BlogID FROM Blog;"
        client.cursor.execute(fetchAllBlogID)
        fetchAllBlogID = [row[0] for row in client.cursor.fetchall()]
        
        print("Generating ddata for BlogRefLink...")
        blogRefLinkData = []
        for blogContentForRefLink in fetchAllBlogID:
            blogRefLinkData.append({
                "BlogRefLink": fake.url(),
                "BlogID": blogContentForRefLink
            })
            
        print("Adding ddata to BlogRefLink...")
        for blogRefLinkContent in blogRefLinkData:
            try:
                client.cursor.execute(InsertBlogRefLink, (
                    blogRefLinkContent["BlogRefLink"],
                    blogRefLinkContent["BlogID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in BlogRefLink table while inserting: {blogRefLinkContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()
        
        # Insert Clinic data
        InsertClinic = """    
            INSERT INTO Clinic (
                ClinicName,
                ClinicAddress,
                ClinicNote,
                ClinicOpenTime,
                ClinicCloseTime,
                created_at
            ) VALUES (%s, %s, %s, %s, %s, NOW())
            ON CONFLICT (ClinicName) 
            DO UPDATE SET
                ClinicNote = EXCLUDED.ClinicNote,
                ClinicOpenTime = EXCLUDED.ClinicOpenTime,
                ClinicCloseTime = EXCLUDED.ClinicCloseTime,
                updated_at = NOW();
        """
        
        print("Generating ddata for Clinic...")
        clinicData = []
        for _ in range(5):
            clinicData.append({
                "ClinicName": fake.company(),
                "ClinicAddress": fake.address(),
                "ClinicNote": fake.sentence(),
                "ClinicOpenTime": fake.time(),
                "ClinicCloseTime": fake.time()
            })

        print("Adding ddata to Clinic...")
        for clinicContent in clinicData:
            try:
                client.cursor.execute(InsertClinic, (
                    clinicContent["ClinicName"],
                    clinicContent["ClinicAddress"],
                    clinicContent["ClinicNote"],
                    clinicContent["ClinicOpenTime"],
                    clinicContent["ClinicCloseTime"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in Clinic table while inserting: {clinicContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()
        
        # Insert Event data
        InsertEvent = """    
            INSERT INTO Event (
                EventName,
                EventDesc,
                EventOrganizer,
                created_at
            ) VALUES (%s, %s, %s, NOW())
            ON CONFLICT (EventID) 
            DO UPDATE SET
                EventDesc = EXCLUDED.EventDesc,
                EventOrganizer = EXCLUDED.EventOrganizer,
                updated_at = NOW();
        """
        
        print("Generating ddata for Event...")
        eventData = []
        for _ in range(5):
            eventData.append({
                "EventName": fake.bs(),
                "EventDesc": fake.sentence(),
                "EventOrganizer": fake.company()
            })

        print("Adding ddata to Event...")
        for eventContent in eventData:
            try:
                client.cursor.execute(InsertEvent, (
                    eventContent["EventName"],
                    eventContent["EventDesc"],
                    eventContent["EventOrganizer"]
                ))
                client.conn.commit()
            except Exception as e:
                print(f"Error in Event table while inserting: {eventContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()
        
        # Insert EventOrganizer data
        InsertEventOrganizer = """    
            INSERT INTO EventOrganizer (
                EventOrganizerName,
                EventID,
                created_at
            ) VALUES (%s, %s, NOW())
            ON CONFLICT (EventOrganizerID) 
            DO UPDATE SET
                updated_at = NOW();
        """
        
        print("Fetching EventID to assign...")
        fetchAllEventID = "SELECT EventID FROM Event;"
        client.cursor.execute(fetchAllEventID)
        fetchAllEventID = [row[0] for row in client.cursor.fetchall()]
        
        print("Generating ddata for EventOrganizer...")
        eventOrgnaizerData = []
        for eventContentForOrganizer in fetchAllEventID:
            eventOrgnaizerData.append({
                "EventOrganizerName": fake.company(),
                "EventID": eventContentForOrganizer
            })

        print("Adding ddata to EventOrganizer...")
        for eventOrgnaizerContent in eventOrgnaizerData:
            try:
                client.cursor.execute(InsertEventOrganizer, (
                    eventOrgnaizerContent["EventOrganizerName"],
                    eventOrgnaizerContent["EventID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in EventOrganizer table while inserting: {eventOrgnaizerContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()
        
        # Insert Journal data
        InsertJournal = """    
            INSERT INTO Journal (
                JournalTitle,
                JournalEmotion,
                JournalContent,
                created_at
            ) VALUES (%s, %s, %s, NOW())
            ON CONFLICT (JournalID)
            DO UPDATE SET
                JournalEmotion = EXCLUDED.JournalEmotion,
                JournalContent = EXCLUDED.JournalContent,
                updated_at = NOW();
        """
        
        print("Generating ddata for Journal...")
        journalData = []
        for _ in range(5):
            journalData.append({
                "JournalTitle": fake.sentence(),
                "JournalEmotion": random.choice(['Happy', 'Sad', 'Excited', 'Angry']),
                "JournalContent": fake.text()
            })

        print("Adding ddata to Journal...")
        for journalContent in journalData:
            try:
                client.cursor.execute(InsertJournal, (
                    journalContent["JournalTitle"],
                    journalContent["JournalEmotion"],
                    journalContent["JournalContent"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in Journal table while inserting: {journalContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()
        
        # Insert JournalCategory data
        InsertJournalCategory = """    
            INSERT INTO JournalCategory (
                JournalCategoryTag,
                JournalID,
                created_at
            ) VALUES (%s, %s, NOW())
            ON CONFLICT (JournalCategoryID) 
            DO UPDATE SET
                updated_at = NOW();
        """
        
        print("Fetching JournalID to assign...")
        fetchAllJournalID = "SELECT JournalID FROM Journal;"
        client.cursor.execute(fetchAllJournalID)
        fetchAllJournalID = [row[0] for row in client.cursor.fetchall()]
        
        print("Generating ddata for JournalCategory...")
        journalCategoryData = []
        for journalContentForCategory in fetchAllJournalID:
            journalCategoryData.append({
                "JournalCategoryTag": fake.bs(),
                "JournalID": journalContentForCategory
            })
            
        print("Adding ddata to JournalCategory...")
        for journalCategoryContent in journalCategoryData:
            try:
                client.cursor.execute(InsertJournalCategory, (
                    journalCategoryContent["JournalCategoryTag"],
                    journalCategoryContent["JournalID"]
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in JournalCategory table while inserting: {journalCategoryContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()
        
        # Insert ContactNumber data
        InsertContactNumber = """    
            INSERT INTO ContactNumber (
                ContactNumber,
                ContactType,
                HealthInstitutionID,
                FinancialInstitutionID,
                EventOrganizerID,
                ClinicID,
                created_at
            ) VALUES (%s, %s, %s, %s, %s, %s, NOW())
            ON CONFLICT (ContactNumberID) 
            DO UPDATE SET
                ContactType = EXCLUDED.ContactType,
                updated_at = NOW();
        """
        
        print("Fetching EventOrganizerID to assign...")
        fetchAllEventOrganizerID = "SELECT EventOrganizerID FROM EventOrganizer;"
        client.cursor.execute(fetchAllEventOrganizerID)
        fetchAllEventOrganizerID = [row[0] for row in client.cursor.fetchall()]
        
        print("Fetching ClinicID to assign...")
        fetchAllClinicID = "SELECT ClinicID FROM Clinic;"
        client.cursor.execute(fetchAllClinicID)
        fetchAllClinicID = [row[0] for row in client.cursor.fetchall()]
        
        contactNumberData = []
        for _ in range(10):
            choice = random.choice(["HealthInstitution", "FinancialInstitution", "EventOrganizer", "Clinic"])
            contactNumberData.append({
                "ContactNumber": fake.phone_number(),
                "ContactType": random.choice(['Mobile', 'Landline']),
                "HealthInstitutionID": None,
                "FinancialInstitutionID": None,
                "EventOrganizerID": None,
                "ClinicID": None
            })
         
            if choice == "HealthInstitution" and allHealthInstitutionIdData:
                contactNumberData[-1]["HealthInstitutionID"] = random.choice(allHealthInstitutionIdData)
            elif choice == "FinancialInstitution" and fetchAllFinancialIntitutionID:
                contactNumberData[-1]["FinancialInstitutionID"] = random.choice(fetchAllFinancialIntitutionID)
            elif choice == "EventOrganizer" and fetchAllEventOrganizerID:
                contactNumberData[-1]["EventOrganizerID"] = random.choice(fetchAllEventOrganizerID)
            elif choice == "Clinic" and fetchAllClinicID:
                contactNumberData[-1]["ClinicID"] = random.choice(fetchAllClinicID)
            else:
                print(f"Warning: No valid IDs found for {choice}. Skipping assignment.")
            
        for contactNumberContent in contactNumberData:
            try:
                client.cursor.execute(InsertContactNumber, (
                    contactNumberContent["ContactNumber"],
                    contactNumberContent["ContactType"],
                    contactNumberContent["HealthInstitutionID"] if contactNumberContent["HealthInstitutionID"] is not None else None,
                    contactNumberContent["FinancialInstitutionID"] if contactNumberContent["FinancialInstitutionID"] is not None else None,
                    contactNumberContent["EventOrganizerID"] if contactNumberContent["EventOrganizerID"] is not None else None,
                    contactNumberContent["ClinicID"] if contactNumberContent["ClinicID"] is not None else None
                ))
                client.conn.commit();
            except Exception as e:
                print(f"Error in ContactNumber table while inserting: {contactNumberContent}")
                print("Exception Type:", type(e).__name__)
                print("Error Message:", e)
                traceback.print_exc()
                client.conn.rollback()

        print("Insert of master data (dummy) is successful!")
        client.conn.close()
        
    except Exception as e:
        print("Unexpected Error occurred.")
        print("Exception Type:", type(e).__name__)
        print("Error Message:", e)
        traceback.print_exc()
        client.conn.rollback()

insertDummyData();