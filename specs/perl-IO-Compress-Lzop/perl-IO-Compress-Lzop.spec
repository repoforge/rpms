# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Compress-Lzop

Summary: Write lzop files/buffers
Name: perl-IO-Compress-Lzop
Version: 2.023
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Compress-Lzop/

Source: http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/IO-Compress-Lzop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Compress::LZO)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Compress::Base) >= 2.023
BuildRequires: perl(IO::Uncompress::Base) >= 2.023
Requires: perl(Compress::LZO)
Requires: perl(IO::Compress::Base) >= 2.023
Requires: perl(IO::Uncompress::Base) >= 2.023

%filter_from_requires /^perl*/d
%filter_setup

%description
Write and read Lzop files of buffers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/IO::Compress::Lzop.3pm*
%doc %{_mandir}/man3/IO::Uncompress::UnLzop.3pm*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/Compress/
%{perl_vendorlib}/IO/Uncompress/

%changelog
* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 2.023-1
- Updated to version 2.023.

* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 2.021-1
- Updated to version 2.021.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.020-1
- Updated to version 2.020.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 2.015-1
- Updated to release 2.015.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 2.011-1
- Updated to release 2.011.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.010-1
- Updated to release 2.010.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.009-1
- Updated to release 2.009.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.008-1
- Updated to release 2.008.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.
