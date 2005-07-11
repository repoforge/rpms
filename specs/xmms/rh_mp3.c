
#include "libxmms/configfile.h"
#include <gtk/gtk.h>
#include "xmms/plugin.h"
#include "xmms/i18n.h"
#include "libxmms/util.h"

static int enabled;
static gpointer foo;

static void init(void)
{
	ConfigFile *cfg;
	
	enabled = 1;
	cfg = xmms_cfg_open_default_file();
        
	xmms_cfg_read_boolean(cfg, "zzmp3", "enabled", &enabled);
	xmms_cfg_free(cfg);
}

static int get_time(void)
{
	return -1;
}


static void clicked_button()
{
	ConfigFile *cfg;
	gchar *filename;
	
	filename = g_strconcat(g_get_home_dir(), "/.xmms/config", NULL);
	cfg = xmms_cfg_open_file(filename);
	if (!cfg)
		cfg = xmms_cfg_new();
	xmms_cfg_write_boolean(cfg, "zzmp3", "enabled", enabled);
	xmms_cfg_write_file(cfg, filename);
	xmms_cfg_free(cfg);
	g_free(filename);
}

static void pref_toggled(void *button)
{
	GtkWidget *check = GTK_WIDGET(button);
	
	if (gtk_toggle_button_get_active(GTK_TOGGLE_BUTTON(check)))
		enabled = 0;
	else
		enabled = 1;
}

static void play_file(char *filename)
{
	GtkWidget *dialog, *vbox, *label, *checkbox, *bbox, *button;
	
	dialog = gtk_dialog_new();
	gtk_window_set_title(GTK_WINDOW(dialog), _("MPEG Layer 1/2/3 Not Supported"));
			     
	vbox = gtk_vbox_new(FALSE, 0);
	gtk_container_set_border_width(GTK_CONTAINER(vbox), 15);
	gtk_box_pack_start(GTK_BOX(GTK_DIALOG(dialog)->vbox), vbox, TRUE, TRUE, 0);
	
	label = gtk_label_new(_("Due to patent licensing, and conflicts between\n"
				"such patent licenses and the licenses of application\n"
				"source code, MPEG-1/2 audio layer 3 (mp3) support has\n"
				"been removed from this application by Red Hat, Inc.\n\n"
				"We apologize for the inconvenience."));
	gtk_box_pack_start(GTK_BOX(vbox), label, TRUE, TRUE, 0);
	
	checkbox = gtk_check_button_new_with_label (_("Do not show this dialog again"));
	gtk_signal_connect_object(GTK_OBJECT(checkbox), "toggled", GTK_SIGNAL_FUNC(pref_toggled), GTK_OBJECT(checkbox));
	gtk_toggle_button_set_active(GTK_TOGGLE_BUTTON(checkbox), TRUE);
	gtk_box_pack_start(GTK_BOX(vbox), checkbox, TRUE, TRUE, 0);
	gtk_widget_show(label);
	gtk_widget_show(checkbox);
	gtk_widget_show(vbox);
	
	bbox = gtk_hbutton_box_new();
	gtk_button_box_set_layout(GTK_BUTTON_BOX(bbox), GTK_BUTTONBOX_SPREAD);
	gtk_button_box_set_spacing(GTK_BUTTON_BOX(bbox), 5);
	gtk_box_pack_start(GTK_BOX(GTK_DIALOG(dialog)->action_area), bbox, FALSE, FALSE, 0);
	
	button = gtk_button_new_with_label(_("Ok"));
	gtk_signal_connect(GTK_OBJECT(button), "clicked", clicked_button, button);
	gtk_signal_connect_object(GTK_OBJECT(button), "clicked", GTK_SIGNAL_FUNC(gtk_widget_destroy), GTK_OBJECT(dialog));
	gtk_box_pack_start(GTK_BOX(bbox), button, FALSE, FALSE, 0);
	GTK_WIDGET_SET_FLAGS(button, GTK_CAN_DEFAULT);
	gtk_widget_grab_default(button);
	gtk_widget_show(button);
	gtk_widget_show(bbox);
	gtk_widget_show(dialog);
	gtk_signal_connect(GTK_OBJECT(dialog), "destroy",
			   GTK_SIGNAL_FUNC(gtk_widget_destroyed), &dialog);
}


static int is_our_file(char *filename)
{
	char *ext;
	guint16 wavid;

	if (!enabled) return FALSE;
	
	if (!strncasecmp(filename, "http://", 7))
	{			/* We assume all http:// (except those ending in .ogg) are mpeg -- why do we do that? */
		ext = strrchr(filename, '.');
		if (ext) 
		{
			if (!strncasecmp(ext, ".ogg", 4)) 
				return FALSE;
			if (!strncasecmp(ext, ".rm", 3) || 
			    !strncasecmp(ext, ".ra", 3)  ||
			    !strncasecmp(ext, ".rpm", 4)  ||
			    !strncasecmp(ext, ".ram", 4))
				return FALSE;
		}
		return TRUE;
	}
	ext = strrchr(filename, '.');
	if (ext)
	{
		if (!strncasecmp(ext, ".mp2", 4) || !strncasecmp(ext, ".mp3", 4))
		{
			return TRUE;
		}
	}
	return FALSE;
}

static void aboutbox(void) {
	static GtkWidget *aboutbox;
	
	if (aboutbox != NULL)
		return;
	
	aboutbox = xmms_show_message(
				     _("MPEG Layer 1/2/3 Placeholder plugin"),
				     _("Placeholder for MPEG Layer 1/2/3, explaining patent issues\n"
				     "Red Hat, Inc."),
				     _("Ok"), FALSE, NULL, NULL);
	gtk_signal_connect(GTK_OBJECT(aboutbox), "destroy",
			   GTK_SIGNAL_FUNC(gtk_widget_destroyed), &aboutbox);
}

InputPlugin zzmp3_ip =
{
	NULL,
	NULL,
	NULL, /* description */
	init,
	aboutbox,
	NULL, /* configure */
	is_our_file,
	NULL,
        play_file,
        NULL, /* stop */
	NULL, /* pause */
	NULL, /* seek */
	NULL, /* set eq */
        get_time, /* get time */
	NULL, NULL, NULL,
	NULL, NULL, NULL, NULL,
	NULL, /* get_song_info */
	NULL, /* file_info_box */
	NULL
};

InputPlugin *get_iplugin_info(void)
{
	zzmp3_ip.description =
		g_strdup(_("MPEG Layer 1/2/3 Placeholder Plugin"));
	return &zzmp3_ip;
}
