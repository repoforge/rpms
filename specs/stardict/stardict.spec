# $Id$
# Authority: dag

Summary: Versatile online dictionary
Name: stardict
Version: 2.4.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://stardict.sourceforge.net/

Source: http://dl.sf.net/stardict/stardict-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.2.0
BuildRequires: scrollkeeper, gcc-c++

Requires(post): scrollkeeper

%description
StarDict is an international dictionary written for the GNOME environment.
It has powerful features such as "Glob-style pattern matching," "Scan
seletion word," "Fuzzy search," etc.

Please select and download dictionaries from:

	http://stardict.cosoft.org.cn/

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/stardict/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/applications/*.desktop
%{_datadir}/stardict/
%{_datadir}/idl/*.idl
%{_datadir}/pixmaps/*
%{_datadir}/omf/stardict/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.4-1.2
- Rebuild for Fedora Core 5.

* Sat Feb 26 2005 Dag Wieers <dag@wieers.com> - 2.4.4-1
- Updated to release 2.4.4.

* Sat May 22 2004 Dag Wieers <dag@wieers.com> - 2.4.3-1
- Updated to release 2.4.3.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 2.4.2-0
- Updated to release 2.4.2.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 2.4.1-0
- Updated to release 2.4.1.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 2.4.0-0
- Updated to release 2.4.0.

* Tue Jul 01 2003 Dag Wieers <dag@wieers.com> - 2.2.1-0
- Updated to release 2.2.1.

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.2.0-0
- Initial package. (using DAR)
