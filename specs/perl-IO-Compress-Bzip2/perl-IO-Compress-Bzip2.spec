# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Compress-Bzip2

Summary: Write bzip2 files/buffers
Name: perl-IO-Compress-Bzip2
Version: 2.011
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Compress-Bzip2/

Source: http://www.cpan.org/modules/by-module/IO/IO-Compress-Bzip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A module for handling bzip2 compressed files.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/IO::Compress::Bzip2.3pm*
%doc %{_mandir}/man3/IO::Uncompress::Bunzip2.3pm*
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Compress/
%{perl_vendorlib}/IO/Compress/Bzip2.pm
%{perl_vendorlib}/IO/Compress/Adapter/
%dir %{perl_vendorlib}/IO/Uncompress/
%{perl_vendorlib}/IO/Uncompress/Bunzip2.pm
%{perl_vendorlib}/IO/Uncompress/Adapter/

%changelog
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
