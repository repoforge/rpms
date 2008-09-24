# $Id$
# Authority: dag
# Upstream: Sheng Chun E<lt>chunzi$cpan,orgE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Lite-TT-HTML

Summary: Create html mail with MIME::Lite and TT
Name: perl-MIME-Lite-TT-HTML
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Lite-TT-HTML/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-Lite-TT-HTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
Requires: perl >= 0:5.6.0

%description
Create html mail with MIME::Lite and TT.

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
%doc Changes LICENSE MANIFEST META.yml README Todo
%doc %{_mandir}/man3/MIME::Lite::TT::HTML.3pm*
%dir %{perl_vendorlib}/MIME/
%dir %{perl_vendorlib}/MIME/Lite/
%dir %{perl_vendorlib}/MIME/Lite/TT/
#%{perl_vendorlib}/MIME/Lite/TT/HTML/
%{perl_vendorlib}/MIME/Lite/TT/HTML.pm

%changelog
* Wed Sep 24 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
