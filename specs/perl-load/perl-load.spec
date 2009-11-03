# $Id$
# Authority: dgehl

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name load

Summary: Control when subroutines will be loaded
Name: perl-load
Version: 0.19
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/load/

Source: http://www.cpan.org/authors/id/E/EL/ELIZABETH/load-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The "load" pragma allows a module developer to give the application
developer more options with regards to optimize for memory or CPU 
usage. The "load" pragma gives more control on the moment when 
subroutines are loaded and start taking up memory. This allows the 
application developer to optimize for CPU usage (by loading all of a
module at compile time and thus reducing the amount of CPU used during
the execution of an application). Or allow the application developer 
to optimize for memory usage, by loading subroutines only when they 
are actually needed, thereby however increasing the amount of CPU 
needed during execution.

%prep
%setup -n %{real_name}-%{version}

%build
%{expand: %%define optflags %{optflags} -fPIC}
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc MANIFEST README CHANGELOG TODO
%doc %{_mandir}/man3/load.3pm*
%{perl_vendorlib}/load.pm

%changelog
* Fri Jun 22 2007 Dominik Gehl <gehl@inverse.ca> - 0.19-1
- Initial package.
