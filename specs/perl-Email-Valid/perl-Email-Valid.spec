# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Valid

Summary: Check validity of Internet email addresses 
Name: perl-Email-Valid
Version: 0.15
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Valid/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MAURICE/Email-Valid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Check validity of Internet email addresses 

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}
%{__rm} -rf %{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Email::Valid.3pm*
%{perl_vendorlib}/Email/Valid.pm

%changelog
* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
