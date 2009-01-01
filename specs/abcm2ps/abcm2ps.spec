# $Id$
# Authority: dries
# Upstream: Jean-Francois <moinejf$free,fr>

Summary: Convert music tunes from ABC format to PostScript
Name: abcm2ps
Version: 5.9.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://moinejf.free.fr/

Source: http://moinejf.free.fr/abcm2ps-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:

%description
abcm2ps is a package that converts music tunes from ABC format to
PostScript. Based on abc2ps version 1.2.5, it was developed mainly
to print baroque organ scores that have independant voices played
on one or more keyboards, and a pedal-board. It introduces many
extensions to the ABC language that make it suitable for classical
music.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall docdir=%{buildroot}%{_datadir}/doc
%{__mv} %{buildroot}%{_datadir}/doc/abcm2ps rpmdocs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL rpmdocs/*
%{_bindir}/abcm2ps
%{_datadir}/abcm2ps/

%changelog
* Thu Jan  1 2009 Dries Verachtert <dries@ulyssis.org> - 5.9.3-1
- Updated to release 5.9.3.

* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 4.12.30-1
- Updated to release 4.12.30.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 4.12.29-1
- Updated to release 4.12.29.

* Mon Feb 12 2007 Dries Verachtert <dries@ulyssis.org> - 4.12.28-1
- Updated to release 4.12.28.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.27-1
- Updated to release 4.12.27.

* Fri Aug 04 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.24-1
- Updated to release 4.12.24.

* Mon Jul 31 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.23-1
- Updated to release 4.12.23.

* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.17-1
- Updated to release 4.12.17.

* Sat Apr 29 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.15-1
- Updated to release 4.12.15.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.14-1
- Updated to release 4.12.14.

* Thu Mar 16 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.11-1
- Updated to release 4.12.11.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.10-1
- Updated to release 4.12.10.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.9-1
- Updated to release 4.12.9.

* Wed Feb 15 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.8-1
- Updated to release 4.12.8.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.7-1
- Updated to release 4.12.7.

* Mon Jan 30 2006 Dries Verachtert <dries@ulyssis.org> - 4.12.6-1
- Updated to release 4.12.6.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 4.12.3-1
- Initial package.
