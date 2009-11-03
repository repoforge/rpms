# $Id$
# Authority: dag
# Upstream: 李凯 <kaili$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jabber-PubSub-JEAI

Summary: Perl module for Erlang's J-EAI server
Name: perl-Jabber-PubSub-JEAI
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jabber-PubSub-JEAI/

Source: http://www.cpan.org/modules/by-module/Jabber/Jabber-PubSub-JEAI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Jabber-PubSub-JEAI is a Perl module for Erlang's J-EAI server.

This package contains the following Perl module:

    Jabber::PubSub::JEAI

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
%doc %{_mandir}/man3/Jabber::PubSub::JEAI.3pm*
%dir %{perl_vendorlib}/Jabber/
%dir %{perl_vendorlib}/Jabber/PubSub/
%{perl_vendorlib}/Jabber/PubSub/JEAI.pm
%dir %{perl_vendorlib}/auto/Jabber/
%dir %{perl_vendorlib}/auto/Jabber/PubSub/
%{perl_vendorlib}/auto/Jabber/PubSub/JEAI/

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
