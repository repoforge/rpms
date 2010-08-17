# $Id$
# Authority: shuff
# Upstream: Khemir Nadim ibn Hamouda <nadim$khemir,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Directory-Scratch-Structured

Summary: creates temporary files and directories from a structured description
Name: perl-Directory-Scratch-Structured
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Directory-Scratch-Structured/

Source: http://search.cpan.org/CPAN/authors/id/N/NK/NKH/Directory-Scratch-Structured-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Directory::Scratch)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Readonly)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
# BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::NoWarnings)
# BuildRequires: perl(Test::Strict)
BuildRequires: perl(Test::Warn)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Data::TreeDumper)
Requires: perl(Directory::Scratch)
Requires: perl(Readonly)
Requires: perl(Sub::Exporter)
Requires: perl(Sub::Install)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module adds a create_structured_tree subroutine to the Directory::Scratch.

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
%{perl_vendorlib}/Directory/Scratch/Structured.pm
#%{perl_vendorlib}/Directory/Scratch/Structured/*
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue Aug 17 2010 Steve Huff <shuff@vecna.org> - 0.04-1
- Initial package.
