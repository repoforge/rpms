# $Id$
# Authority: dag
# Upstream: Chris Williams <chris$bingosnet,co,uk>

### EL6 ships with perl-Archive-Tar-1.58-115.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-Archive-Tar.noarch 1:1.39.1-1.el5_5.2 (RHN)
%{?el5:# Tag: rfx}
### EL4 ships with perl-Archive-Tar-1.39.1-1.el4_8.2
%{?el4:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Tar

Summary: Archive-Tar module for perl
Name: perl-Archive-Tar
Version: 1.56
Release: 2%{?dist}
Epoch: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Tar/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/Archive-Tar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(Compress::Zlib) >= 2.015
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(IO::Compress::Base) >= 2.015
BuildRequires: perl(IO::Compress::Bzip2) >= 2.015
BuildRequires: perl(IO::Compress::Gzip) >= 2.015
BuildRequires: perl(IO::Zlib) >= 1.01
BuildRequires: perl(Package::Constants)
BuildRequires: perl(Test::Harness) >= 2.26
BuildRequires: perl(Test::More)
Requires: perl(Compress::Zlib) >= 2.015
Requires: perl(File::Spec) >= 0.82
Requires: perl(IO::Compress::Base) >= 2.015
Requires: perl(IO::Compress::Bzip2) >= 2.015
Requires: perl(IO::Compress::Gzip) >= 2.015
Requires: perl(IO::Zlib) >= 1.01
Requires: perl(Package::Constants)
Requires: perl(Test::Harness) >= 2.26
Requires: perl(Test::More)
Requires: perl >= 0:5.00503

%filter_from_requires /^perl*/d
%filter_setup


%description
Module for manipulations of tar archives.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man1/ptar.1*
%doc %{_mandir}/man1/ptardiff.1*
%doc %{_mandir}/man3/Archive::Tar.3pm*
%doc %{_mandir}/man3/Archive::Tar::File.3pm*
%{_bindir}/ptar
%{_bindir}/ptardiff
%dir %{perl_vendorlib}/Archive/
%{perl_vendorlib}/Archive/Tar/
%{perl_vendorlib}/Archive/Tar.pm

%changelog
* Sat Mar 12 2011 Yury V. Zaytsev <yury@shurup.com> - 1.56-2
- Added epoch to follow upstream (thanks to Dave Miller!)

* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.56-1
- Updated to version 1.56.

* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.54-1
- Updated to version 1.54.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.32-1
- Updated to release 1.32.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Updated to release 1.30.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.08-0
- Initial package. (using DAR)
