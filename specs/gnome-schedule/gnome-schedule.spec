# $Id$
# Authority: dag
# Upstream: Philip Van Hoof <me$freax,org>

Summary: Graphical configuration tool for cron
Name: gnome-schedule
Version: 1.0.0
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://gnome-schedule.sourceforge.net/

Source: http://dl.sf.net/gnome-schedule/gnome-schedule-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
### FIXME: We need yelp now to *build* gnome-schedule ?
BuildRequires: python, yelp, pygtk2 >= 2.3, gnome-python2
BuildRequires: pkgconfig, pygtk2-devel, glib2-devel, gettext
# configure checks for crontab and for at
BuildRequires: vixie-cron, at, gnome-doc-utils
Requires: python, pygtk2 >= 2.3, gnome-python2, vixie-cron, at

%description
Gnome-schedule is a GNOME GUI for configuring a users crontab. It was made
for Vixie cron whom comes with Fedora Linux, but should work with other
cron servers as well if the format of the config file is similar. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/gnome-schedule
%{_datadir}/applications/gnome-schedule.desktop
%{_datadir}/gnome-schedule/
%{_datadir}/pixmaps/gnome-schedule.png

%changelog
* Wed Jan 04 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Sat Aug 06 2005 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Updated to release 0.9.0.

* Sat Nov 13 2004 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Updated to release 0.1.0.

* Fri Aug 13 2004 Dag Wieers <dag@wieers.com> - 0.0.1-1
- Initial package. (using DAR)
