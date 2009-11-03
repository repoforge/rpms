# $Id$
# Authority: dag

Summary: Mambo Open Source (CMS)
Name: mambo
Version: 4.6
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.mamboserver.com/

Source0: http://mamboxchange.com/frs/download.php/7877/MamboV%{version}.tar.gz
Source1: http://mamboxchange.com/frs/download.php/7967/Mambov454_Security_Patch1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: file
Requires: httpd, php >= 4.1.2, php-mysql >= 4.1.2

%description
Mambo SiteServer is a dynamic Web content management tool that is capable of
building sites from several pages to several thousand. It comes complete with
10 built-in modules, a WYSIWYG editor, site statistics, an admin interface,
multi language support, custom module support, and more. 

%package administrator
Summary: Administrative web interface for Mambo Open Source
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}

%description administrator
Administrative web interface for Mambo Open Source

%prep
%setup -c -a 1

### Remove CVS leftover files
find . -type d -name CVS | xargs %{__rm} -rf
find . -type f -name '.cvs*' -o -name '.#*' | xargs %{__rm} -rf

### Fix permissions
find . -type d | xargs %{__chmod} 0755
find . -type f | xargs %{__chmod} 0644

### Convert to Unix files
#find . -type f -name '*.html' -o -name '*.php' -o -name '*.xml' | xargs -n1 dos2unix --keepdate
find . -type f -name '*.html' -o -name '*.php' -o -name '*.xml' | xargs -n1 %{__perl} -pi -e 's|\r$||'

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_localstatedir}/www/mambo/
%{__cp} -av * %{buildroot}%{_localstatedir}/www/mambo/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_localstatedir}/www/mambo/{LICENSE,README}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, apache, apache, 0755)
%doc LICENSE README
# if added, the web installer won't work.
#%config(noreplace) %attr(0644,root,root) %{webroot}/%{name}/configuration.php
%{_localstatedir}/www/mambo/
%exclude %{_localstatedir}/www/mambo/administrator/

%files administrator
%defattr(-, apache, apache, 0755)
%{_localstatedir}/www/mambo/administrator/

%changelog
* Sun Oct 15 2006 Dag Wieers <dag@wieers.com> - 4.6-1
- Updated to release 4.6.

* Sat Oct 14 2006 Dag Wieers <dag@wieers.com> - 4.5.4-3
- Fixed group name.

* Thu Jun 29 2006 Dag Wieers <dag@wieers.com> - 4.5.4-2
- Change ownership to apache.

* Mon Jun 26 2006 Dag Wieers <dag@wieers.com> - 4.5.4-1
- Initial package. (using DAR)
