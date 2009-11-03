# $Id$
# Authority: dag
# Upstream: <gtranslator-devel$lists,sf,net>

Summary: Gettext po file editor
Name: gtranslator
Version: 1.1.6
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://gtranslator.sourceforge.net/

#Source: http://dl.sf.net/gtranslator/gtranslator-%{version}.tar.gz
Source: http://ftp.gnome.org/pub/GNOME/sources/gtranslator/1.1/gtranslator-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scrollkeeper >= 0.1.4
BuildRequires: glib2-devel >= 2.0, gtk2-devel >= 2.0, libxml2-devel => 2.4
BuildRequires: libgnomeui-devel >= 1.105, libbonoboui-devel >= 1.108
BuildRequires: libgnomecanvas-devel >= 1.112, gnome-vfs2-devel >= 1.9.4
BuildRequires: GConf2-devel >= 1.2, gettext, perl(XML::Parser)
BuildRequires: gtkspell-devel

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
gtranslator is a comfortable po file editor with many bells and whistles.
It features many useful function which ease the work of translators of po
files imminently.

%prep
%setup

### FIXME: Improve desktop-file entry according to standards (Please fix upstream)
%{__perl} -pi.orig -e '
		s|^_(Name)=.*$|$1=Translation Editor|;
		s|^_(Comment)=.*$|$1=Translate GUI applications|;
	' data/desktop/gtranslator.desktop.in

%build
%configure
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} check

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

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
%{_bindir}/gtranslator
%{_bindir}/pozilla.sh
%{_datadir}/applications/gtranslator.desktop
%{_datadir}/gtranslator/
%{_datadir}/mime-info/gtranslator.mime
%{_datadir}/mime-info/gtranslator.keys
%{_datadir}/omf/gtranslator/
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/gtranslator/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.6-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 1.1.6-1
- Updated to release 1.1.6.

* Sun Jul 25 2004 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Updated to release 1.1.5.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

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
