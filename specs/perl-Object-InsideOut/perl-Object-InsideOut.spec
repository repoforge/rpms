# $Id$
# Authority: dag
# Upstream: Jerry D. Hedden <jdhedden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-InsideOut

Summary: Perl module with comprehensive inside-out object support module
Name: perl-Object-InsideOut
Version: 3.14
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-InsideOut/

Source: http://www.cpan.org/modules/by-module/Object/Object-InsideOut-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Bundle/
%dir %{perl_vendorlib}/Bundle/Object/
%{perl_vendorlib}/Bundle/Object/InsideOut.pm
%dir %{perl_vendorlib}/Object/
%{perl_vendorlib}/Object/InsideOut/
%{perl_vendorlib}/Object/InsideOut.pm
%{perl_vendorlib}/Object/InsideOut.pod

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 3.14-1
- Initial package. (using DAR)
