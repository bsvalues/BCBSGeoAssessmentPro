import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    logger.info("Initializing Supabase environment")
    from set_supabase_env import ensure_supabase_env
    
    # Set up Supabase environment variables
    ensure_supabase_env()
    
    # Get the current environment
    from supabase_env_manager import get_current_environment, is_configured
    
    env = get_current_environment() or "development"
    configured = is_configured()
    
    logger.info(f"Supabase environment: {env}")
    logger.info(f"Supabase configured: {configured}")
except Exception as e:
    logger.warning(f"Failed to initialize Supabase environment: {str(e)}")
    logger.warning("Continuing without Supabase configuration")

# Set BYPASS_LDAP environment variable to true for development
os.environ['BYPASS_LDAP'] = 'true'

from app import app  # noqa: F401

