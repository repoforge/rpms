# $Id$
# Authority: dag
# Upstream: Ken Youens-Clark <kclark$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-RecordParser
%define real_version 1.002001

Summary: Parse record-oriented data in a text file
Name: perl-Text-RecordParser
Version: 1.2.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-RecordParser/

Source: http://www.cpan.org/modules/by-module/Text/Text-RecordParser-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Parse record-oriented data in a text file.

%prep
%setup -n %{real_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
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
%doc Changes INSTALL MANIFEST META.yml README TODO
%doc %{_mandir}/man1/tablify.1*
%doc %{_mandir}/man1/tabmerge.1*
%doc %{_mandir}/man3/Text::RecordParser.3pm*
%doc %{_mandir}/man3/Text::RecordParser::Tab.3pm*
%{_bindir}/tablify
%{_bindir}/tabmerge
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/RecordParser/
%{perl_vendorlib}/Text/RecordParser.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Initial package. (using DAR)
