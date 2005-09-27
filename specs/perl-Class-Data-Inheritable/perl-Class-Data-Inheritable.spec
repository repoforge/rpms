# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Data-Inheritable

Summary: Class-Data-Inheritable module for perl
Name: perl-Class-Data-Inheritable
Version: 0.02
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Data-Inheritable/

Source: http://www.cpan.org/modules/by-module/Class/Class-Data-Inheritable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Class-Data-Inheritable module for perl

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Data/
%dir %{perl_vendorlib}/Class/Data/Inheritable.pm

%changelog
* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.02-1
Initial package. (using DAR)
