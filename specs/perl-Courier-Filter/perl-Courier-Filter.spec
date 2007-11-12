# $Id$
# Authority: dag
# Upstream: Julian Mehnle <julian$mehnle,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Courier-Filter

Summary: A purely Perl-based mail filter framework for the Courier MTA
Name: perl-Courier-Filter
Version: 0.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Courier-Filter/

Source: http://www.cpan.org/authors/id/J/JM/JMEHNLE/courier-filter/Courier-Filter-%{version}.tar.gz
Source1: pureperlfilter.conf
Patch0: Courier-Filter-Build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.8 
BuildRequires: perl(Error)
BuildRequires: perl(Test::Simple)

%description
A purely Perl-based mail filter framework for the Courier MTA.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL installdirs="vendor"
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
./Build install destdir="%{buildroot}" create_packlist="1"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL MANIFEST META.yml README SIGNATURE TODO examples/
%doc %{_mandir}/man3/Courier::Config.3pm*
%dir %{perl_vendorlib}/Courier/
#%{perl_vendorlib}/Courier/Filter/
%{perl_vendorlib}/Courier/Filter.pm

%changelog
* Mon Nov 12 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Initial package. (using DAR)
