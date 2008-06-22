# $Id$
# Authority: dag
# Upstream: Jerry D. Hedden <jdhedden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-InsideOut

Summary: Comprehensive inside-out object support module
Name: perl-Object-InsideOut
Version: 3.42
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-InsideOut/

Source: http://www.cpan.org/modules/by-module/Object/Object-InsideOut-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Object-InsideOut is a Perl module with comprehensive inside-out
object support module.

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
%doc %{_mandir}/man3/Bundle::Object::InsideOut.3pm*
%doc %{_mandir}/man3/Object::InsideOut.3pm*
%doc %{_mandir}/man3/Object::InsideOut::*.3pm*
%dir %{perl_vendorlib}/Bundle/
%dir %{perl_vendorlib}/Bundle/Object/
%{perl_vendorlib}/Bundle/Object/InsideOut.pm
%dir %{perl_vendorlib}/Object/
%{perl_vendorlib}/Object/InsideOut/
%{perl_vendorlib}/Object/InsideOut.pm
%{perl_vendorlib}/Object/InsideOut.pod

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 3.42-1
- Updated to release 3.42.

* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 3.39-1
- Updated to release 3.39.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 3.38-1
- Updated to release 3.38.

* Fri Feb 22 2008 Dag Wieers <dag@wieers.com> - 3.37-1
- Updated to release 3.37.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 3.36-1
- Updated to release 3.36.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 3.35-1
- Updated to release 3.35.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 3.34-1
- Updated to release 3.34.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 3.33-1
- Updated to release 3.33.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 3.27-1
- Updated to release 3.27.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 3.14-1
- Initial package. (using DAR)
