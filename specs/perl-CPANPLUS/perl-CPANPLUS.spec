# $Id$

# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define real_name CPANPLUS
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Command-line access to the CPAN interface
Name: perl-CPANPLUS
Version: 0.051
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CPANPLUS/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KANE/CPANPLUS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The "CPANPLUS" library is an API to the "CPAN" mirrors and a collection
of interactive shells, commandline programs, daemons, etc, that use
this API.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi -e 's|^ *\@ARGV = grep \{.*||g;' Makefile.PL
%{__perl} -pi -e 's|use Your::Module::Here|your use statements here|g;' lib/CPANPLUS/Internals/Constants/Report.pm
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix} AUTOINSTALL=1 SETUP=0
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} \
  %{buildroot}%{perl_vendorarch} \
  %{buildroot}%{_mandir}/man3/CPANPLUS*Win32* \
  %{buildroot}%{perl_vendorlib}/CPANPLUS/inc/*/*/*Win32*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{perl_vendorlib}/CPANPLUS.pm
%{perl_vendorlib}/CPANPLUS/*

%changelog
* Mon Jan 17 2005 Dries Verachtert <dries@ulyssis.org> - 0.051-1
- Initial package.

