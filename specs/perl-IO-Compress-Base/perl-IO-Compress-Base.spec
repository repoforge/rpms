# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Compress-Base

Summary: Base Class for IO::Compress modules
Name: perl-IO-Compress-Base
Version: 2.015
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Compress-Base/

Source: http://www.cpan.org/modules/by-module/IO/IO-Compress-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Base Class for IO::Compress modules.

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
%doc %{_mandir}/man3/File::GlobMapper.3pm*
%doc %{_mandir}/man3/IO::Compress::Base.3pm*
%doc %{_mandir}/man3/IO::Uncompress::Base.3pm*
%doc %{_mandir}/man3/IO::Uncompress::AnyUncompress.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/GlobMapper.pm
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Compress/
%{perl_vendorlib}/IO/Compress/Base/
%{perl_vendorlib}/IO/Compress/Base.pm
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Uncompress/
%{perl_vendorlib}/IO/Uncompress/Base.pm
%{perl_vendorlib}/IO/Uncompress/AnyUncompress.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.015-1
- Updated to release 2.015.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 2.011-1
- Updated to release 2.011.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.010-1
- Updated to release 2.010.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.009-1
- Updated to release 2.009.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.008-1
- Updated to release 2.008.

* Mon Nov 12 2007 Dag Wieers <dag@wieers.com> - 2.006-1
- Updated to release 2.006.

* Wed Aug 08 2007 Dag Wieers <dag@wieers.com> - 2.005-1
- Updated to release 2.005.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.

