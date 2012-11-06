# Authority: N/A
# Upstream: N/A

Summary: GTK frontent for gnunet
Name: gnunet-gtk
Version: 0.9.4
Release: 1%{?dist}
License: GPL
Group: Applications/Network
URL: http://gnunet.org/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: glade
Requires: gnunet = %{version}
Requires: gtk3
Requires: libextractor

BuildRequires: glade-devel
BuildRequires: gnunet-devel = %{version}
BuildRequires: gtk3-devel
BuildRequires: libextractor-devel

%description
GTK gui for the gnunet p2p network system

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__rm} %{buildroot}/%{_datadir}/doc/gnunet/COPYING
%{__rm} %{buildroot}/%{_datadir}/doc/gnunet/README
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README 
%{_bindir}/gnunet-fs-gtk
%{_bindir}/gnunet-peerinfo-gtk
%{_bindir}/gnunet-setup
%{_bindir}/gnunet-statistics-gtk
%{_includedir}/gnunet-gtk/gnunet_gtk.h
%{_libdir}/libgnunetgtk.la
%{_libdir}/libgnunetgtk.so
%{_libdir}/libgnunetgtk.so.1
%{_libdir}/libgnunetgtk.so.1.1.0
%{_datadir}/applications/gnunet-fs-gtk.desktop
%{_datadir}/applications/gnunet-setup.desktop
%{_datadir}/gnunet-gtk/downloaded.gif
%{_datadir}/gnunet-gtk/downloading.gif
%{_datadir}/gnunet-gtk/downloading_not_receiving.gif
%{_datadir}/gnunet-gtk/error.gif
%{_datadir}/gnunet-gtk/flags/*.png
%{_datadir}/gnunet-gtk/found_source.gif
%{_datadir}/gnunet-gtk/gnunet-setup-oxygen-cancel.png
%{_datadir}/gnunet-gtk/gnunet-setup-oxygen-ok.png
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_about_window.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_create_namespace_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_download_as_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_edit_publication.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_main_window.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_namespace_manager.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_open_directory_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_open_url_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_progress_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_publish_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_publish_directory_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_publish_file_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_publish_tab.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_search_tab.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_select_pseudonym_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_fs_gtk_unindex.glade
%{_datadir}/gnunet-gtk/gnunet_gtk_status_bar_menu.glade
%{_datadir}/gnunet-gtk/gnunet_logo.png
%{_datadir}/gnunet-gtk/gnunet_peerinfo_gtk_about_window.glade
%{_datadir}/gnunet-gtk/gnunet_peerinfo_gtk_main_window.glade
%{_datadir}/gnunet-gtk/gnunet_setup_calendar_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_setup_gtk_main_window.glade
%{_datadir}/gnunet-gtk/gnunet_setup_qr_save_as_dialog.glade
%{_datadir}/gnunet-gtk/gnunet_statistics_gtk_about_window.glade
%{_datadir}/gnunet-gtk/gnunet_statistics_gtk_main_window.glade
%{_datadir}/gnunet-gtk/green.png
%{_datadir}/gnunet-gtk/published.gif
%{_datadir}/gnunet-gtk/publishing.gif
%{_datadir}/gnunet-gtk/qr_dummy.png
%{_datadir}/gnunet-gtk/red.png
%{_datadir}/gnunet-gtk/searching_sources.gif
%{_datadir}/gnunet/config.d/gnunet-fs-gtk.conf
%{_datadir}/icons/hicolor/16x16/apps/gnunet-fs-gtk.png
%{_datadir}/icons/hicolor/22x22/apps/gnunet-fs-gtk.png
%{_datadir}/icons/hicolor/24x24/apps/gnunet-fs-gtk.png
%{_datadir}/icons/hicolor/32x32/apps/gnunet-fs-gtk.png
%{_datadir}/icons/hicolor/scalable/apps/gnunet-fs-gtk.svg
%{_datadir}/locale/da/LC_MESSAGES/gnunet-gtk.mo
%{_datadir}/locale/de/LC_MESSAGES/gnunet-gtk.mo
%{_datadir}/locale/fr/LC_MESSAGES/gnunet-gtk.mo
%{_datadir}/locale/sv/LC_MESSAGES/gnunet-gtk.mo
%{_datadir}/locale/tr/LC_MESSAGES/gnunet-gtk.mo
%{_datadir}/locale/vi/LC_MESSAGES/gnunet-gtk.mo
%{_mandir}/man1/gnunet-fs-gtk.1.gz
%{_mandir}/man1/gnunet-peerinfo-gtk.1.gz
%{_mandir}/man1/gnunet-setup.1.gz
%{_mandir}/man1/gnunet-statistics-gtk.1.gz


%changelog
* Tue Nov 06 2012 Christoph Maser <cmaser@gm.de>
- Initial package.
