# $Id$
# Authority: cmr
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Compress

Summary: IO Interface to compressed data files/buffers
Name: perl-IO-Compress
Version: 2.030
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Compress/

Source: http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/IO-Compress-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Compress::Raw::Bzip2) = 2.024
BuildRequires: perl(Compress::Raw::Zlib) = 2.024
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Compress::Raw::Bzip2) = 2.024
Requires: perl(Compress::Raw::Zlib) = 2.024
Requires: perl(Scalar::Util)
 
Obsoletes: perl-Compress-Zlib
Obsoletes: perl-IO-Compress-Bzip2
Obsoletes: perl-IO-Compress-Base
Obsoletes: perl-IO-Compress-Zlib

%filter_from_requires /^perl*/d
%filter_setup

%description
IO Interface to compressed data files/buffers.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Compress::Zlib.3pm*
%doc %{_mandir}/man3/File::GlobMapper.3pm*
%doc %{_mandir}/man3/IO::Compress*.3pm*
%doc %{_mandir}/man3/IO::Uncompress*.3pm*
%dir %{perl_vendorlib}/IO/
#%{perl_vendorlib}/auto/Compress/Zlib/autosplit.ix
%{perl_vendorlib}/Compress/Zlib.pm
%{perl_vendorlib}/File/GlobMapper.pm
%{perl_vendorlib}/IO/Compress/
%{perl_vendorlib}/IO/Uncompress/

%changelog
* Thu Sep 23 2010 David Hrbáč <david@hrbac.cz> - 2.030-1
- new upstream release

* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 2.024-1
- Updated to version 2.024.

* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 2.023-1
- Updated to version 2.023.

* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 2.021-1
- Updated to version 2.021.

* Sat Jul 04 2009 Chritoph Maser <cmr@financial.com> - 2.020-2
- Obsoletes perl-Compress-Zlib, perl-IO-Compress-Zlib

* Sat Jul 04 2009 Chritoph Maser <cmr@financial.com> - 2.020-1
- Initial package. (using DAR)
