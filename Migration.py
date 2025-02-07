import client
# from data.masterdata import health_institution, financial_institution

# Data Definition Language : commands, which are used to create,
# alter, and delete database objects like tables, views, indexes,
# and users; key examples of DDL commands include: CREATE, ALTER,
# DROP, and TRUNCATE

def createTable():
    Create_table_query="""
        CREATE TABLE  if not exists HealthInstitution (
            HealthInstitutionID bigint primary key generated always as identity,
            HealthInstitutionName text NOT NULL UNIQUE,
            HealthInstitutionDesc text NOT NULL,
            HealthInstitutionEmailAddress text NOT NULL,
            HealthInstitutionOpenTime text NOT NULL,
            HealthInstitutionCloseTime text NOT NULL,
            HealthInstitutionType text NOT NULL,
            HealthInstitutionAddress text NOT NULL,
            HealthInstitutionAddressLong float NOT NULL,
            HealthInstitutionAddressLat float NOT NULL,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
            
        CREATE TABLE  if not exists HealthInstitutionService (
            HealthInstitutionServiceID bigint primary key generated always as identity,
            HealthInstitutionServiceName text NOT NULL,
            HealthInstitutionServiceDesc text NOT NULL,
            HealthInstitutionID bigint NOT NULL,
            FOREIGN KEY (HealthInstitutionID) REFERENCES HealthInstitution(HealthInstitutionID) ON DELETE CASCADE,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
            
        CREATE TABLE  if not exists HealthInstitutionAcreditedInsurance (
            HealthInstitutionAcreditedInsuranceID bigint primary key generated always as identity,
            HealthInstitutionAcreditedInsuranceName text NOT NULL,
            HealthInstitutionAcreditedInsuranceDesc text NOT NULL,
            HealthInstitutionID bigint NOT NULL,
            FOREIGN KEY (HealthInstitutionID) REFERENCES HealthInstitution(HealthInstitutionID) ON DELETE CASCADE,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
            
        CREATE TABLE if not exists FinancialInstitution (
            FinancialInstitutionID bigint primary key generated always as identity,
            FinancialInstitutionName text NOT NULL UNIQUE,
            FinancialInstitutionDesc text NOT NULL,
            FinancialInstitutionEmailAddress text NOT NULL,
            FinancialInstitutionOpenTime text NOT NULL,
            FinancialInstitutionCloseTime text NOT NULL,
            FinancialInstitutionType text NOT NULL,
            FinancialInstitutionAddress text NOT NULL,
            FinancialInstitutionAddressLong float,
            FinancialInstitutionAddressLat float,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
            
        CREATE TABLE if not exists FinancialInstitutionNote (
            FinancialInstitutionNoteID bigint primary key generated always as identity,
            FinancialInstitutionNoteName text NOT NULL,
            FinancialInstitutionNoteDesc text NOT NULL,
            FinancialInstitutionID bigint NOT NULL,
            FOREIGN KEY (FinancialInstitutionID) REFERENCES FinancialInstitution(FinancialInstitutionID) ON DELETE CASCADE,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
            
        CREATE TABLE if not exists FinancialInstitutionBenefit (
            FinancialInstitutionBenefitID bigint primary key generated always as identity,
            FinancialInstitutionBenefitName text NOT NULL,
            FinancialInstitutionBenefitDesc text NOT NULL,
            FinancialInstitutionID bigint NOT NULL,
            FOREIGN KEY (FinancialInstitutionID) REFERENCES FinancialInstitution(FinancialInstitutionID) ON DELETE CASCADE,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
            
        CREATE TABLE if not exists FinancialInstitutionProcess (
            FinancialInstitutionProcessID bigint primary key generated always as identity,
            FinancialInstitutionProcessDesc text NOT NULL,
            FinancialInstitutionBenefitID bigint NOT NULL,
            FOREIGN KEY (FinancialInstitutionBenefitID) REFERENCES FinancialInstitutionBenefit(FinancialInstitutionBenefitID) ON DELETE CASCADE,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
            
        CREATE TABLE if not exists BenefitInclusion (
            BenefitInclusionID bigint primary key generated always as identity,
            BenefitInclusionTitle text NOT NULL,
            BenefitInclusionDesc text NOT NULL,
            FinancialInstitutionBenefitID bigint NOT NULL,
            FOREIGN KEY (FinancialInstitutionBenefitID) REFERENCES FinancialInstitutionBenefit(FinancialInstitutionBenefitID) ON DELETE CASCADE,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
        
        CREATE TABLE if not exists FinancialInstitutionRequirement (
            FinancialInstitutionRequirementID bigint primary key generated always as identity,
            FinancialInstitutionRequirementName text NOT NULL,
            FinancialInstitutionRequirementDesc text NOT NULL,
            FinancialInstitutionRequirementType text NOT NULL,
            FinancialInstitutionBenefitID bigint NOT NULL,
            FOREIGN KEY (FinancialInstitutionBenefitID) REFERENCES FinancialInstitutionBenefit(FinancialInstitutionBenefitID) ON DELETE CASCADE,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
        
        CREATE TABLE if not exists Blog (
            BlogID bigint primary key generated always as identity,
            BlogName text NOT NULL,
            BlogAuthor text NOT NULL,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
        
        CREATE TABLE if not exists BlogRefLink (
            BlogRefLinkID bigint primary key generated always as identity,
            BlogRefLink text NOT NULL,
            BlogID bigint NOT NULL,
            FOREIGN KEY (BlogID) REFERENCES Blog(BlogID) ON DELETE CASCADE,
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
        
        CREATE TABLE IF NOT EXISTS Clinic (
            ClinicID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            ClinicName TEXT NOT NULL UNIQUE,
            ClinicAddress TEXT NOT NULL,
            ClinicNote TEXT,
            ClinicOpenTime TEXT NOT NULL,
            ClinicCloseTime TEXT NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP
        );
        
        
        CREATE TABLE IF NOT EXISTS Event (
            EventID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            EventName TEXT NOT NULL,
            EventDesc TEXT NOT NULL,
            EventOrganizer TEXT NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS EventOrganizer (
            EventOrganizerID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            EventOrganizerName TEXT NOT NULL,
            EventID BIGINT NOT NULL,
            FOREIGN KEY (EventID) REFERENCES Event(EventID) ON DELETE CASCADE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS Journal (
            JournalID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            JournalTitle TEXT NOT NULL,
            JournalEmotion TEXT NOT NULL,
            JournalContent TEXT NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS JournalCategory (
            JournalCategoryID BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            JournalCategoryTag TEXT NOT NULL,
            JournalID BIGINT NOT NULL,
            FOREIGN KEY (JournalID) REFERENCES Journal(JournalID) ON DELETE CASCADE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP
        );
        
        Create TABLE if not exists ContactNumber (
            ContactNumberID bigint primary key generated always as identity,
            ContactNumber text NOT NULL,
            ContactType text,
            
            HealthInstitutionID bigint NULL,
            FinancialInstitutionID bigint NULL,
            EventOrganizerID bigint NULL,
            ClinicID bigint NULL,
            
            CHECK (
                (HealthInstitutionID IS NOT NULL)::int +
                (FinancialInstitutionID IS NOT NULL)::int +
                (EventOrganizerID IS NOT NULL)::int +
                (ClinicID IS NOT NULL)::int = 1
            ),
            
            CONSTRAINT FK_HealthInstitution FOREIGN KEY (HealthInstitutionID) REFERENCES HealthInstitution(HealthInstitutionID) ON DELETE CASCADE,
            CONSTRAINT FK_FinancialInstitution FOREIGN KEY (FinancialInstitutionID) REFERENCES FinancialInstitution(FinancialInstitutionID) ON DELETE CASCADE,
            CONSTRAINT FK_Clinic FOREIGN KEY (ClinicID) REFERENCES Clinic(ClinicID) ON DELETE RESTRICT,
            CONSTRAINT FK_EventOrganizer FOREIGN KEY (EventOrganizerID) REFERENCES EventOrganizer(EventOrganizerID) ON DELETE CASCADE,
            
            created_at timestamp with time zone DEFAULT now(),
            updated_at timestamp
        );
        
        """

    client.cursor.execute(Create_table_query)

    client.conn.commit()
    print("created table successfully")

def enableRLS():

    # Syntax:
    # ALTER TABLE <Table_name> ENABLE ROW LEVEL SECURITY;

    enable_RLS="""
    
    ALTER TABLE HealthInstitution ENABLE ROW LEVEL SECURITY;
    -- ALTER TABLE healthinstitution ADD CONSTRAINT unique_healthinstitution_name UNIQUE (healthinstitutionname);

    ALTER TABLE HealthInstitutionService ENABLE ROW LEVEL SECURITY;
    ALTER TABLE HealthInstitutionAcreditedInsurance ENABLE ROW LEVEL SECURITY;
    ALTER TABLE FinancialInstitution ENABLE ROW LEVEL SECURITY;
    -- ALTER TABLE financialinstitution ADD CONSTRAINT unique_financialinstitution_name UNIQUE (financialinstitutionname);
    ALTER TABLE FinancialInstitutionNote ENABLE ROW LEVEL SECURITY;
    ALTER TABLE FinancialInstitutionBenefit ENABLE ROW LEVEL SECURITY;
    ALTER TABLE FinancialInstitutionProcess ENABLE ROW LEVEL SECURITY;
    ALTER TABLE BenefitInclusion ENABLE ROW LEVEL SECURITY;
    ALTER TABLE FinancialInstitutionRequirement ENABLE ROW LEVEL SECURITY;
    ALTER TABLE Blog ENABLE ROW LEVEL SECURITY;
    ALTER TABLE BlogRefLink ENABLE ROW LEVEL SECURITY;
    ALTER TABLE Clinic ENABLE ROW LEVEL SECURITY;
    ALTER TABLE ContactNumber ENABLE ROW LEVEL SECURITY;
    ALTER TABLE Journal ENABLE ROW LEVEL SECURITY;
    ALTER TABLE JournalCategory ENABLE ROW LEVEL SECURITY;
    ALTER TABLE Event ENABLE ROW LEVEL SECURITY;
    ALTER TABLE EventOrganizer ENABLE ROW LEVEL SECURITY;
    """

    client.cursor.execute(enable_RLS)
    client.conn.commit()
    print("RLS(Row Level Security) enabled successfully");

def injectPolicies():

    # Syntax:
    # CREATE POLICY <Name_Of_Policy> ON <Table_Name> FOR SELECT USING (true);


    policyInjectionQuery = """
    
    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on HealthInstitution
    CREATE POLICY full_HealthInstitution_select ON HealthInstitution FOR SELECT USING (true);
    CREATE POLICY full_HealthInstitution_insert ON HealthInstitution FOR INSERT WITH CHECK (true);
    CREATE POLICY full_HealthInstitution_update ON HealthInstitution FOR UPDATE USING (true);
    CREATE POLICY full_HealthInstitution_delete  ON HealthInstitution FOR DELETE USING (true);
    
    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on FinancialInstitution
    CREATE POLICY full_FinancialInstitution_select ON FinancialInstitution FOR SELECT USING (true);
    CREATE POLICY full_FinancialInstitution_insert ON FinancialInstitution FOR INSERT WITH CHECK (true);
    CREATE POLICY full_FinancialInstitution_update ON FinancialInstitution FOR UPDATE USING (true);
    CREATE POLICY full_FinancialInstitution_delete ON FinancialInstitution FOR DELETE USING (true);
    
    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on HealthInstitutionService
    CREATE POLICY full_HealthInstitutionService_select ON HealthInstitutionService FOR SELECT USING (true);
    CREATE POLICY full_HealthInstitutionService_insert ON HealthInstitutionService FOR INSERT WITH CHECK (true);
    CREATE POLICY full_HealthInstitutionService_update ON HealthInstitutionService FOR UPDATE USING (true);
    CREATE POLICY full_HealthInstitutionService_delete ON HealthInstitutionService FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on HealthInstitutionAcreditedInsurance
    CREATE POLICY full_HealthInstitutionAcreditedInsurance_select ON HealthInstitutionAcreditedInsurance FOR SELECT USING (true);
    CREATE POLICY full_HealthInstitutionAcreditedInsurance_insert ON HealthInstitutionAcreditedInsurance FOR INSERT WITH CHECK (true);
    CREATE POLICY full_HealthInstitutionAcreditedInsurance_update ON HealthInstitutionAcreditedInsurance FOR UPDATE USING (true);
    CREATE POLICY full_HealthInstitutionAcreditedInsurance_delete ON HealthInstitutionAcreditedInsurance FOR DELETE USING (true);
    
    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on FinancialInstitutionNote
    CREATE POLICY full_FinancialInstitutionNote_select ON FinancialInstitutionNote FOR SELECT USING (true);
    CREATE POLICY full_FinancialInstitutionNote_insert ON FinancialInstitutionNote FOR INSERT WITH CHECK (true);
    CREATE POLICY full_FinancialInstitutionNote_update ON FinancialInstitutionNote FOR UPDATE USING (true);
    CREATE POLICY full_FinancialInstitutionNote_delete ON FinancialInstitutionNote FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on FinancialInstitutionBenefit
    CREATE POLICY full_FinancialInstitutionBenefit_select ON FinancialInstitutionBenefit FOR SELECT USING (true);
    CREATE POLICY full_FinancialInstitutionBenefit_insert ON FinancialInstitutionBenefit FOR INSERT WITH CHECK (true);
    CREATE POLICY full_FinancialInstitutionBenefit_update ON FinancialInstitutionBenefit FOR UPDATE USING (true);
    CREATE POLICY full_FinancialInstitutionBenefit_delete ON FinancialInstitutionBenefit FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on FinancialInstitutionProcess
    CREATE POLICY full_FinancialInstitutionProcess_select ON FinancialInstitutionProcess FOR SELECT USING (true);
    CREATE POLICY full_FinancialInstitutionProcess_insert ON FinancialInstitutionProcess FOR INSERT WITH CHECK (true);
    CREATE POLICY full_FinancialInstitutionProcess_update ON FinancialInstitutionProcess FOR UPDATE USING (true);
    CREATE POLICY full_FinancialInstitutionProcess_delete ON FinancialInstitutionProcess FOR DELETE USING (true);
    
    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on FinancialInstitutionRequirement
    CREATE POLICY full_FinancialInstitutionRequirement_select ON FinancialInstitutionRequirement FOR SELECT USING (true);
    CREATE POLICY full_FinancialInstitutionRequirement_insert ON FinancialInstitutionRequirement FOR INSERT WITH CHECK (true);
    CREATE POLICY full_FinancialInstitutionRequirement_update ON FinancialInstitutionRequirement FOR UPDATE USING (true);
    CREATE POLICY full_FinancialInstitutionRequirement_delete ON FinancialInstitutionRequirement FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on BenefitInclusion
    CREATE POLICY full_BenefitInclusion_select ON BenefitInclusion FOR SELECT USING (true);
    CREATE POLICY full_BenefitInclusion_insert ON BenefitInclusion FOR INSERT WITH CHECK (true);
    CREATE POLICY full_BenefitInclusion_update ON BenefitInclusion FOR UPDATE USING (true);
    CREATE POLICY full_BenefitInclusion_delete ON BenefitInclusion FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on Blog
    CREATE POLICY full_Blog_select ON Blog FOR SELECT USING (true);
    CREATE POLICY full_Blog_insert ON Blog FOR INSERT WITH CHECK (true);
    CREATE POLICY full_Blog_update ON Blog FOR UPDATE USING (true);
    CREATE POLICY full_Blog_delete ON Blog FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on BlogRefLink
    CREATE POLICY full_BlogRefLink_select ON BlogRefLink FOR SELECT USING (true);
    CREATE POLICY full_BlogRefLink_insert ON BlogRefLink FOR INSERT WITH CHECK (true);
    CREATE POLICY full_BlogRefLink_update ON BlogRefLink FOR UPDATE USING (true);
    CREATE POLICY full_BlogRefLink_delete ON BlogRefLink FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on ContactNumber
    CREATE POLICY full_ContactNumber_select ON ContactNumber FOR SELECT USING (true);
    CREATE POLICY full_ContactNumber_insert ON ContactNumber FOR INSERT WITH CHECK (true);
    CREATE POLICY full_ContactNumber_update ON ContactNumber FOR UPDATE USING (true);
    CREATE POLICY full_ContactNumber_delete ON ContactNumber FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on Journal
    CREATE POLICY full_Journal_select ON Journal FOR SELECT USING (true);
    CREATE POLICY full_Journal_insert ON Journal FOR INSERT WITH CHECK (true);
    CREATE POLICY full_Journal_update ON Journal FOR UPDATE USING (true);
    CREATE POLICY full_Journal_delete ON Journal FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on JournalCategory
    CREATE POLICY full_JournalCategory_select ON JournalCategory FOR SELECT USING (true);
    CREATE POLICY full_JournalCategory_insert ON JournalCategory FOR INSERT WITH CHECK (true);
    CREATE POLICY full_JournalCategory_update ON JournalCategory FOR UPDATE USING (true);
    CREATE POLICY full_JournalCategory_delete ON JournalCategory FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on Event
    CREATE POLICY full_Event_select ON Event FOR SELECT USING (true);
    CREATE POLICY full_Event_insert ON Event FOR INSERT WITH CHECK (true);
    CREATE POLICY full_Event_update ON Event FOR UPDATE USING (true);
    CREATE POLICY full_Event_delete ON Event FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on EventOrganizer
    CREATE POLICY full_EventOrganizer_select ON EventOrganizer FOR SELECT USING (true);
    CREATE POLICY full_EventOrganizer_insert ON EventOrganizer FOR INSERT WITH CHECK (true);
    CREATE POLICY full_EventOrganizer_update ON EventOrganizer FOR UPDATE USING (true);
    CREATE POLICY full_EventOrganizer_delete ON EventOrganizer FOR DELETE USING (true);

    -- Allow all users to SELECT, INSERT, UPDATE, DELETE on Clinic
    CREATE POLICY full_Clinic_select ON Clinic FOR SELECT USING (true);
    CREATE POLICY full_Clinic_insert ON Clinic FOR INSERT WITH CHECK (true);
    CREATE POLICY full_Clinic_update ON Clinic FOR UPDATE USING (true);
    CREATE POLICY full_Clinic_delete ON Clinic FOR DELETE USING (true);
    """

    client.cursor.execute(policyInjectionQuery)
    client.conn.commit()
    print("RLS(Row Level Security) policy Injected successfully");
    client.cursor.close()

def dropTable():
    deleteTableQuery="""
        DROP TABLE IF EXISTS BlogRefLink CASCADE;
        DROP TABLE IF EXISTS JournalCategory CASCADE;
        DROP TABLE IF EXISTS EventOrganizer CASCADE;
        DROP TABLE IF EXISTS ContactNumber CASCADE;
        DROP TABLE IF EXISTS BenefitInclusion CASCADE;
        DROP TABLE IF EXISTS FinancialInstitutionProcess CASCADE;
        DROP TABLE IF EXISTS FinancialInstitutionBenefit CASCADE;
        DROP TABLE IF EXISTS FinancialInstitutionNote CASCADE;
        DROP TABLE IF EXISTS FinancialInstitutionRequirement CASCADE;
        DROP TABLE IF EXISTS HealthInstitutionService CASCADE;
        DROP TABLE IF EXISTS HealthInstitutionAcreditedInsurance CASCADE;
        DROP TABLE IF EXISTS Clinic CASCADE;
        DROP TABLE IF EXISTS Event CASCADE;
        DROP TABLE IF EXISTS Journal CASCADE;
        DROP TABLE IF EXISTS Blog CASCADE;
        DROP TABLE IF EXISTS FinancialInstitution CASCADE;
        DROP TABLE IF EXISTS HealthInstitution CASCADE;
    """

    client.cursor.execute(deleteTableQuery)
    client.conn.commit()
    print("Table Delete successfully")
    client.cursor.close()
    
def truncateTable():
    truncateQuery = """
    
    """

# Data Manipulation Language : Data Definition Language actually consists
# of the SQL commands that can be used to defining, altering, and deleting
# database structures such as tables, indexes, and schemas. It simply deals
# with descriptions of the database schema and is used to create and modify
# the structure of database objects in the database

# Transaction Control Language: Transactions group a set of tasks into
# a single execution unit. Each transaction begins with a specific task
# and ends when all the tasks in the group are successfully completed.
# If any of the tasks fail, the transaction fails.

# def begin_transaction():

# def commit_changes():

# def undo_changes():

# def set_Savepoint():

# createTable();
# enableRLS();
# injectPolicies();
# dropTable();