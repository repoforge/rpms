# $Id$
# Authority: shuff
# Upstream: A. R. Ferreira <ferreira$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Shell-Perl

Summary: A read-eval-print loop in Perl
Name: perl-%{real_name}
Version: 0.0018
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Shell-Perl/

Source: http://search.cpan.org/CPAN/authors/id/F/FE/FERREIRA/Shell-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Term::ReadLine)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Class::Accessor)
Requires: perl(File::Basename)
Requires: perl(File::HomeDir)
Requires: perl(File::Slurp)
Requires: perl(Getopt::Long)
Requires: perl(IPC::Cmd)
Requires: perl(Path::Class)
Requires: perl(Term::ReadLine)
Requires: rpm-macros-rpmforge

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This is the implementation of a command-line interpreter for Perl. I wrote this
because I was tired of using irb when needing a calculator with a real language
within. Ah, that and because it was damn easy to write it.

This module is the heart of the pirl script provided with Shell-Perl
distribution, along with this module.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Shell/
%{perl_vendorlib}/Shell/*
%{_bindir}/*

%changelog
* Mon Jan 04 2010 Steve Huff <shuff@vecna.org> - 0.0018-1
- Initial package.
