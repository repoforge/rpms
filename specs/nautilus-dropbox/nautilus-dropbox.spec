# $Id$
# Authority: shuff
# Upstream: Dropbox Support (https://www.dropbox.com/ticket)

Summary: Sync and backup files between computers
Name: nautilus-dropbox
Version: 0.6.7
Release: 1%{?dist}
License: Proprietary
Group: Applications/File
URL: http://www.dropbox.com/

Source: http://linux.dropbox.com/packages/nautilus-dropbox-%{version}.tar.bz2
Patch0: nautilus-dropbox-0.6.7-pygtk.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.12
BuildRequires: gtk2-devel >= 2.12
BuildRequires: libnotify-devel >= 0.4.4
BuildRequires: nautilus-devel >= 2.16
BuildRequires: pygtk2-devel
Requires: dropbox

# there are binaries in this package, don't mess with them
%define __os_install_post %{nil}

%description
Dropbox is software that syncs your files online and across your computers.

Put your files into your Dropbox on one computer, and they'll be instantly
available on any of your other computers that you've installed Dropbox on
(Windows, Mac, and Linux too!) Because a copy of your files are stored on
Dropbox's secure servers, you can also access them from any computer or mobile
device using the Dropbox website.


%description -n nautilus-dropbox
Dropbox is software that syncs your files online and across your computers.

%prep
%setup
%patch0 -p0

%build
### Sucks, but have no alternative :-/
export DISPLAY=localhost:10.0
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
/sbin/ldconfig
/usr/bin/update-desktop-database || :
touch --no-create /usr/share/icons/hicolor
/usr/bin/gtk-update-icon-cache -q /usr/share/icons/hicolor || :

for I in /home/*/.dropbox-dist; do
   # require a minimum version of 0.7.110
   DROPBOX_VERSION="$I/VERSION"
   if [[ -f "$DROPBOX_VERSION" ]]; then
     DROPBOX_VERSION_MAJOR=$(cat "$DROPBOX_VERSION" | cut -d. -f1)
     DROPBOX_VERSION_MINOR=$(cat "$DROPBOX_VERSION" | cut -d. -f2)
     DROPBOX_VERSION_MICRO=$(cat "$DROPBOX_VERSION" | cut -d. -f3)

     if (( $DROPBOX_VERSION_MAJOR <= 0 && $DROPBOX_VERSION_MINOR <= 7 && $DROPBOX_VERSION_MICRO < 110 )); then
       # stop dropbox
       dropbox stop &>/dev/null
       sleep 0.5
       killall dropbox &>/dev/null
       killall dropboxd &>/dev/null

       rm -rf "$I"
     fi
   fi
done

for pid in $(pgrep -x nautilus); do
   # Extract the display variable so that we can show a box.
   # Hope they have xauth to localhost. 
   export `cat /proc/$pid/environ | tr "\0" "\n" | grep DISPLAY`

   zenity --question --timeout=30 --title=Dropbox --text='The Nautilus File Browser has to be restarted. Any open file browser windows will be closed in the  process. Do this now?' > /dev/null 2>&1
   if [ $? -eq 0 ] ; then
     echo "Killing nautilus"
     kill $pid
   fi
 done

 if ! pgrep -x dropbox > /dev/null 2>&1 ;  then
   zenity --info --timeout=5 --text='Dropbox installation successfully completed! You can start Dropbox from your applications menu.' > /dev/null 2>&1
   if [ $? -ne 0 ]; then
       echo
       echo 'Dropbox installation successfully completed! You can start Dropbox from your applications menu.'
   fi
 fi

%postun
/sbin/ldconfig
/usr/bin/update-desktop-database || :
touch --no-create /usr/share/icons/hicolor
/usr/bin/gtk-update-icon-cache -q /usr/share/icons/hicolor || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/dropbox.1*
%{_datadir}/applications/dropbox.desktop
%{_datadir}/icons/hicolor/*/apps/dropbox.png
%{_datadir}/nautilus-dropbox/emblems/emblem-dropbox-*.icon
%{_datadir}/nautilus-dropbox/emblems/emblem-dropbox-*.png
%{_libdir}/nautilus/extensions-2.0/libnautilus-dropbox.so
%exclude %{_bindir}/dropbox
%exclude %{_libdir}/nautilus/extensions-2.0/libnautilus-dropbox.a
%exclude %{_libdir}/nautilus/extensions-2.0/libnautilus-dropbox.la

%changelog
* Tue Apr 26 2011 Dag Wieers <dag@wieers.com> - 0.6.7-1
- Initial package. (using DAR)
