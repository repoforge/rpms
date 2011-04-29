# $Id$
# Authority: shuff
# Upstream: osfameron <osfameron$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Tags

Summary: Generate (possibly exuberant) Ctags-style tags for Perl
Name: perl-Perl-Tags
Version: 0.28
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-Tags/

Source: http://search.cpan.org/CPAN/authors/id/O/OS/OSFAMERON/Perl-Tags-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Locate)
BuildRequires: perl(PPI)
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Data::Dumper)
Requires: perl(File::Find)
Requires: perl(File::Spec)
Requires: perl(File::Temp)
Requires: perl(Module::Locate)
Requires: perl(PPI)
Requires: rpm-macros-rpmforge

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Generate (possibly exuberant) Ctags style tags for Perl sourcecode.
Recursively follows use and require statements, up to a maximum of max_level.

The implemented tagger, Perl::Tags::Naive is a more-or-less straight ripoff,
slightly updated, of the original pltags code, and is rather naive. It should
be possible to subclass using something like PPI or Text::Balanced, though be
aware that this is alpha software and the internals are subject to change (so
get in touch to let me know what you want to do and I'll try to help).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/Perl/Tags.pm
%{perl_vendorlib}/Perl/Tags/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Apr 29 2011 Steve Huff <shuff@vecna.org> - 0.28-1
- Initial package.
