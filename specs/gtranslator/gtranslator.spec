# $Id$

# Authority: dag

Summary: GNOME po file editor with many bells and whistles
Name: gtranslator
Version: 1.0
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.gtranslator.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://dl.sf.net/gtranslator/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: scrollkeeper >= 0.1.4
BuildRequires: glib2-devel >= 2.0, gtk2-devel >= 2.0, libxml2-devel => 2.4
BuildRequires: libgnomeui-devel >= 1.105, libbonoboui-devel >= 1.108
BuildRequires: libgnomecanvas-devel >= 1.112, gnome-vfs2-devel >= 1.9.4
BuildRequires: GConf2-devel >= 1.2

Requires(post): scrollkeeper

%description
gtranslator is a comfortable po file editor with many bells and whistles.
It features many useful function which ease the work of translators of po
files imminently.

%prep
%setup

%build
%configure \
	--enable-mime-bind="yes" \
	--with-gconf
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} check

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	SC_OMFDIR="%{buildroot}%{_datadir}/omf"
%find_lang %{name}

### Cleean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post 
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/gtranslator/
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/gtranslator/
%{_datadir}/mime-info/*
%{_datadir}/omf/gtranslator/
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/gtranslator/

%changelog
* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 1.0-0.pre1
- Updated to release 1.0pre1.

* Fri Jun 27 2003 Dag Wieers <dag@wieers.com> - 1.0-0.cvs20030626
- Updated to release 1.0CVS-20030626.

* Sat Jun 14 2003 Dag Wieers <dag@wieers.com> - 0.99-0
- Updated to release 0.99.

* Tue Mar 18 2003 Dag Wieers <dag@wieers.com> - 0.43-0
- Initial package. (using DAR)
