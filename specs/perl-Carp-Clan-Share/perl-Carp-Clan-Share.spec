# $Id$
# Authority: shuff
# Upstream: Robert Krimen <robertkrimen$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Carp-Clan-Share

Summary: Share your Carp::Clan settings with your whole Clan
Name: perl-Carp-Clan-Share
Version: 0.013
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Carp-Clan-Share/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKRIMEN/Carp-Clan-Share-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp::Clan)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This is a very lightweight helper module (actually just an import method) that
will automagically create a __PACKAGE__::Carp module for you.

Any arguments passed to the import (e.g. via use) method are forwarded along to
Carp::Clan.

NOTE: If you use this from a package ending with ::Carp, then it will use the
parent of of that package as the target namespace.

%prep
%setup -n %{real_name}-%{version}

# damn it Module::Install
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\\.42.*/ && s/6\\.3\\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Carp/Clan/Share.pm
#%{perl_vendorlib}/Carp/Clan/Share/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Wed Mar 30 2011 Steve Huff <shuff@vecna.org> - 0.013-1
- Initial package.
