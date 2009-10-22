# $Id$
# Authority: shuff
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Romana-Perligata

Summary: Perl in Latin
Name: perl-%{real_name}
Version: 0.50
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Romana-Perligata/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Lingua-Romana-Perligata-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Filter::Util::Call)

%filter_from_requires /^perl*/d
%filter_setup

%description
The Lingua::Romana::Perligata makes it makes it possible to write Perl programs
in Latin. (If you have to ask "Why?", then the answer probably won't make any
sense to you either.)

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Lingua
%{perl_vendorlib}/Lingua/*

%changelog
* Wed Oct 21 2009 Steve Huff <shuff@vecna.org> - 0.50-1
- Initial package.
