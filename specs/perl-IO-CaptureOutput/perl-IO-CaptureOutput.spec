# $Id$
# Authority: dag
# Upstream: Simon Flack <sf AT flacks,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-CaptureOutput

Summary: IO-CaptureOutput module for perl
Name: perl-IO-CaptureOutput
Version: 1.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-CaptureOutput/

Source: http://www.cpan.org/modules/by-module/IO/IO-CaptureOutput-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
IO-CaptureOutput module for perl.

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
%doc %{_mandir}/man3/IO::CaptureOutput.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/IO/
#%{perl_vendorlib}/IO/CaptureOutput/
%{perl_vendorlib}/IO/CaptureOutput.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
