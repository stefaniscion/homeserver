def snapraid_scrub():
    logging.info("Launching snapraid scrub...")
    os.system("snapraid scrub")
    logging.info("Done.")