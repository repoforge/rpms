# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name the

Summary: This is teh, best module evar!
Name: perl-the
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/the/

Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/the-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
Requires: perl >= 1:5.6.1

%description
This is teh, best module evar!.

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
%doc %{_mandir}/man3/a.3pm*
%doc %{_mandir}/man3/an.3pm*
%doc %{_mandir}/man3/more.3pm*
%doc %{_mandir}/man3/teh.3pm*
%doc %{_mandir}/man3/the.3pm*
#%{perl_vendorlib}/the/
%{perl_vendorlib}/a.pm
%{perl_vendorlib}/an.pm
%{perl_vendorlib}/more.pm
%{perl_vendorlib}/teh.pm
%{perl_vendorlib}/the.pm

%changelog
* Fri Nov 19 2010 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
