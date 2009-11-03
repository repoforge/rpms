# $Id$
# Authority: dag

%define real_version 0.33

Summary: Tool to maintain translations anywhere
Name: po4a
Version: 0.33.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://alioth.debian.org/projects/po4a/

Source: http://alioth.debian.org/frs/download.php/2376/po4a-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext
BuildRequires: perl(Locale::gettext) >= 1.01
BuildRequires: perl(Module::Build)
BuildRequires: perl(SGMLS) >= 1.03ii
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Text::WrapI18N)
Requires: gettext

%description
The po4a (po for anything) project goal is to ease translations (and
more interestingly, the maintenance of translations) using gettext
tools on areas where they were not expected like documentation.

%prep
%setup -n %{name}-%{real_version}

%build
%{__perl} Build.PL --installdirs vendor
./Build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Ugly fix to get the translated man pages in utf-8
for file in  %{buildroot}%{_mandir}/*/man*/*.gz; do
    gunzip -c $file | iconv -f latin1 -t utf8 | gzip -c > $file.new
    mv -f $file.new $file
done

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README* TODO
%doc %{_mandir}/man1/msguntypot.1*
%doc %{_mandir}/man1/po4a*.1*
%doc %{_mandir}/man3/Locale::Po4a::*.3pm*
%doc %{_mandir}/man7/po4a.7*
%doc %{_mandir}/*/man1/msguntypot.1*
%doc %{_mandir}/*/man1/po4a*.1*
%doc %{_mandir}/*/man3/Locale::Po4a::*.3pm*
%doc %{_mandir}/*/man7/po4a.7*
%{_bindir}/po4a*
%{_bindir}/msguntypot
%{perl_vendorlib}/Locale/

%changelog
* Wed Oct 29 2008 Dag Wieers <dag@wieers.com> - 0.33.2-1
- Initial package. (using DAR)
