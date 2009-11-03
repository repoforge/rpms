# $Id$
# Authority: dries
# Upstream: Mark Summerfield <summer$perlpress,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-MacroScript

Summary: Macro pre-processor with embedded perl capability
Name: perl-Text-MacroScript
Version: 1.38
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-MacroScript/

Source: http://www.cpan.org/modules/by-module/Text/Text-MacroScript-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Define macros, scripts and variables in macro files or directly in text
files.

Commands may appear in separate macro files which are loaded in either via
the text files they process (e.g. via the %LOAD command), or may be embedded
directly in text files. Almost every command that can appear in a file has
an equivalent object method so that programmers may achieve the same things
in code as can be achieved by macro commands in texts; there are also
additional methods which have no command equivalents.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/MacroScript.pm
%{perl_vendorlib}/Text/macroutil.pl

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.38-1
- Initial package.
