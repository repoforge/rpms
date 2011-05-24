# $Id$
# Authority: shuff
# Upstream: Troels Liebe Bentsen <troels@infopro.dk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Privileges-Drop

Summary: make it simple to drop process privileges
Name: perl-Privileges-Drop
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Privileges-Drop/

Source: http://search.cpan.org/CPAN/authors/id/T/TL/TLBDK/Privileges-Drop-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.0
BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.0
Requires: perl(Carp)
Requires: perl(English)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module tries to simplify the process of dropping privileges. This can be
useful when your Perl program needs to bind to privileged ports, etc. This
module is much like Proc::UID, except that it's implemented in pure Perl.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Build.PL \
    --installdirs="vendor" \
    --prefix="%{buildroot}%{_prefix}"

%install
%{__rm} -rf %{buildroot}
./Build pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog META.yml README examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Privileges/Drop.pm
#%{perl_vendorlib}/Privileges/Drop/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Tue May 24 2011 Steve Huff <shuff@vecna.org> - 1.01-1
- Initial package.
