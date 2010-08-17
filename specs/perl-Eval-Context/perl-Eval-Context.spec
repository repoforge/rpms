# $Id$
# Authority: shuff
# Upstream: Khemir Nadim ibn Hamouda <nadim$khemir,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Eval-Context

Summary: Evalute Perl code in context wrapper
Name: perl-Eval-Context
Version: 0.09.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Eval-Context/

Source: http://search.cpan.org/CPAN/authors/id/N/NK/NKH/Eval-Context-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Compare)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Directory::Scratch::Structured)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Package::Generator)
BuildRequires: perl(Readonly)
BuildRequires: perl(Safe) >= 2.16
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Symbol)
# BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Output)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Text::Diff)
BuildRequires: perl(version) >= 0.5
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Data::Compare)
Requires: perl(Data::Dumper)
Requires: perl(Data::TreeDumper)
Requires: perl(File::Slurp)
Requires: perl(Module::Build::Compat)
Requires: perl(Package::Generator)
Requires: perl(Readonly)
Requires: perl(Safe) >= 2.16
Requires: perl(Sub::Exporter)
Requires: perl(Sub::Install)
Requires: perl(Symbol)
Requires: perl(version) >= 0.5

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module define a subroutine that let you evaluate Perl code in a specific
context. The code can be passed directly as a string or as a file name to read
from. It also provides some subroutines to let you define and optionally share
variables and subroutines between your code and the code you wish to evaluate.
Finally there is some support for running your code in a safe compartment.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README Todo.txt
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Eval/Context.pm
#%{perl_vendorlib}/Eval/Context/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Aug 17 2010 Steve Huff <shuff@vecna.org> - 0.09.11-1
- Initial package.
