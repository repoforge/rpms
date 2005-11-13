# $Id$
# Authority: dries
# Upstream: Andreas J. Konig <andreas,koenig$anima,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Symdump

Summary: Dump symbol names or the symbol table
Name: perl-Devel-Symdump
Version: 2.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Symdump/

Source: http://search.cpan.org/CPAN/authors/id/A/AN/ANDK/Devel-Symdump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl

%description
Dump symbol names or the symbol table.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Devel/Symdump.pm
%dir %{perl_vendorlib}/Devel/Symdump/
%{perl_vendorlib}/Devel/Symdump/Export.pm

%changelog
* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
