# $Id$
# Authority: shuff
# Upstream: Jonathan Rockway <jrockway$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Directory-Scratch

Summary: Easy-to-use self-cleaning scratch space
Name: perl-Directory-Scratch
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Directory-Scratch/

Source: http://search.cpan.org/CPAN/authors/id/J/JR/JROCKWAY/Directory-Scratch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Slurp) >= 9999.12
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::stat)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(File::Copy)
Requires: perl(File::Path)
Requires: perl(File::Slurp) >= 9999.12
Requires: perl(File::Spec)
Requires: perl(File::Temp)
Requires: perl(File::stat)
Requires: perl(Path::Class)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
When writing test suites for modules that operate on files, it's often
inconvenient to correctly create a platform-independent temporary storage
space, manipulate files inside it, then clean it up when the test exits. The
inconvenience usually results in tests that don't work everwhere, or worse, no
tests at all.

This module aims to eliminate that problem by making it easy to do things
right.

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
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Directory/Scratch.pm
#%{perl_vendorlib}/Directory/Scratch/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Aug 17 2010 Steve Huff <shuff@vecna.org> - 0.14-1
- Initial package.
