# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Which

Summary: Portable implementation of the `which' utility
Name: perl-File-Which
Version: 0.05
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Which/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PEREINAR/File-Which-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Portable implementation of the `which' utility.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/Which.pm
%{_bindir}/pwhich

%changelog
* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
