# $Id$
# Authority: dries
# Upstream: Steve Hancock <shancock7078$bigfoot,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Tidy

Summary: Parses and beautifies perl source
Name: perl-Tidy
Version: 
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-Tidy/

Source: http://www.cpan.org/modules/by-module/Perl/Perl-Tidy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perltidy is a tool to indent and reformat perl scripts. It can also
write scripts in html format.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc README CHANGES
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/perltidy
%dir %{perl_vendorlib}/Perl/
%{perl_vendorlib}/Perl/Tidy.pm

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - -1
- Updated to release .

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 20031021-1
- Initial package.
