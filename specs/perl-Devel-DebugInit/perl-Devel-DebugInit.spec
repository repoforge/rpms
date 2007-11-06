# $Id$
# Authority: dries
# Upstream: Jason E. Stewart <jason_e_stewart$users,sf,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-DebugInit

Summary: Create debugger initialization files from C header file macros
Name: perl-Devel-DebugInit
Version: 0.3
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-DebugInit/

Source: http://search.cpan.org/CPAN/authors/id/J/JA/JASONS/Devel-DebugInit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Devel::DebugInit is aimed at C/C++ developers who want access to C
macro definitions from within a debugger. It provides a simple and
automated way of creating debugger initialization files for a specific
project. The initialization files created contain user-defined
functions built from the macro definitions in the project's header
files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Devel/DebugInit.pm
%{perl_vendorlib}/Devel/DebugInit

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
