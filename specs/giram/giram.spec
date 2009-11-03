# $Id$
# Authority: dag
# Upstream: David Odin <David$dindinx,org>

%define major 0.3

Summary: POV-Ray oriented modeller
Name: giram
Version: 0.3.5
Release: 0.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://www.giram.org/

Source: http://www.giram.org/downloads/giram-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0, glib2-devel >= 2.0, gettext

%description
Giram is a Persistance Of Vision (POV-Ray) oriented modeller.

%prep
%setup

%build
%configure
%{__perl} -pi.orig -e '
		s|^giramdatadir = .+$|giramdatadir = \$(datadir)/giram/%{major}|;
		s|^giramplugindir = .+$|giramplugindir = \$(libdir)/giram/%{major}|;
		s|^giramsysconfdir = .+$|giramsysconfdir = \$(sysconfdir)/giram/%{major}|;
		s|^helpfilepath = .+$|helpfilepath = \$(docdir)/giram|;
	' Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libexecdir}/*.a \
		%{buildroot}%{_libexecdir}/*.la
%{__rm} -rf %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ANNOUNCE AUTHORS BUGS ChangeLog CONTRIBUTORS COPYING HACKING IDEAS NEWS README TODO
%doc docs/README* docs/Tutorial* samples/ tips/*.txt
%doc %{_mandir}/man?/*
%dir %{_sysconfdir}/giram/
%dir %{_libexecdir}/giram/
#dir %{_libdir}/giram/
%dir %{_datadir}/giram/
%config %{_sysconfdir}/giram/%{major}/
%{_bindir}/*
%{_libexecdir}/*.so
%{_libexecdir}/giram/
%{_datadir}/giram/%{major}/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.5-0.2
- Rebuild for Fedora Core 5.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.3.5-0
- Initial package. (using DAR)
