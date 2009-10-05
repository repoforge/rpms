# $Id$
# Authority: shuff
# Upstream: Yves Agostini <agostini$univ-metz,fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jifty-Plugin-OpenID

Summary: Provides OpenID authentication for your jifty app
Name: perl-%{real_name}
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jifty-Plugin-OpenID/

Source: http://search.cpan.org/CPAN/authors/id/Y/YV/YVESAGO/Jifty-Plugin-OpenID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Cache::FileCache)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Jifty)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Net::OpenID::Consumer)
Requires: perl(LWP::UserAgent)

# we don't want to either provide or require anything from _docdir, per policy
%filter_provides_in %{_docdir}
%filter_requires_in %{_docdir}

# it is not strictly necessary to use LWPx::ParanoidAgent
%filter_from_requires /^perl(LWPx.*/d
%filter_from_requires /^perl(Jifty::Plugin::OpenID.*/d
%filter_setup

%description
OpenID authentication for Jifty applications.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Jifty/Plugin/
%{perl_vendorlib}/Jifty/Plugin/*


%changelog
* Mon Oct 05 2009 Steve Huff <shuff@vecna.org> - 1.00-1
- Initial package.

