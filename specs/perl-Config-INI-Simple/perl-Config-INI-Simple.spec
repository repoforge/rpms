# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-INI-Simple

Summary: Simple reading and writing from an INI file
Name: perl-Config-INI-Simple
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-INI-Simple/

Source: http://www.cpan.org/modules/by-module/Config/Config-INI-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 4:5.8.7

%description
Simple reading and writing from an INI file, with preserved comments too!

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
%doc Changes Changes~ MANIFEST README
%doc %{_mandir}/man3/Config::INI::Simple.3pm*
%dir %{perl_vendorlib}/Config/
%dir %{perl_vendorlib}/Config/INI/
#%{perl_vendorlib}/Config/INI/Simple/
%{perl_vendorlib}/Config/INI/Simple.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
