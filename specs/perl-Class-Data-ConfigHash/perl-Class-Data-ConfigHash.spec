# $Id$
# Authority: shuff
# Upstream: Daisuke Maki <daisuke$endeworks,jp>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Data-ConfigHash

Summary: Add Catalyst-style config to your class
Name: perl-Class-Data-ConfigHash
Version: 0.00002
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Data-ConfigHash/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/Class-Data-ConfigHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Class::Data::Inheritable)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
I often times find myself wanting a per-class config that can be used to
provide sane class-level defaults, but with the ability to easily customize the
values at run time.

The idea is that you can hardcode the defaults in your class, but you can also
easily override them by merging the original hash with a newly given hash. This
feature is handled beautifully in Catalyst.

So there, this module is basically that feature from Catalyst ripped out to a
separate module so it can be used elsewhere.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

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
%doc Changes META.yml
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Class/Data/ConfigHash.pm
#%{perl_vendorlib}/Class/Data/ConfigHash/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Mon Jun 20 2011 Steve Huff <shuff@vecna.org> - 0.00002-1
- Initial package.
