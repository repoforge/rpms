# $Id$
# Authority: dries
# Upstream: Jeff Gilchrist <pbzip2$compression,ca>

Summary: Parallel implementation of bzip2
Name: pbzip2
Version: 1.0.3
Release: 1
License: BSD
Group: Applications/File
URL: http://compression.ca/pbzip2/

Source: http://compression.ca/pbzip2/pbzip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, bzip2-devel

%description
PBZIP2 is a parallel implementation of the bzip2 block- sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.

%prep
%setup
%{__perl} -npi -e "s|.PREFIX./man|(PREFIX)/share/man|g;" Makefile
%{__perl} -npi -e "s|..PREFIX./bin/pbzip2( ..PREFIX./bin/pbunzip2)|%{_bindir}/pbzip2 \1|g;" Makefile
%{__perl} -npi -e "s|..PREFIX./bin/pbzip2( ..PREFIX./bin/pbzcat)|%{_bindir}/pbzip2 \1|g;" Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man1/pbzip2.1*
%{_bindir}/pbzip2
%{_bindir}/pbunzip2
%{_bindir}/pbzcat

%changelog
* Mon Nov 24 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sat Jul 28 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Apr 01 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Mon Mar 19 2007 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Initial package.
