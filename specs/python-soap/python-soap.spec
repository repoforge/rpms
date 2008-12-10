# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name SOAPpy

Summary: Full-featured SOAP library for Python
Name: python-soap
Version: 0.11.6
Release: 1
License: Python Software Foundation License
Group: Development/Languages
URL: http://pywebsvcs.sourceforge.net

Source: http://dl.sf.net/pywebsvcs/SOAPpy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-fpconst >= 0.6.0
Requires: python-fpconst >= 0.6.0
Requires: PyXML >= 0.8.3
Obsoletes: SOAPpy <= %{version}-%{release}
Provides: SOAPpy = %{version}-%{release}
Obsoletes: python-SOAPpy <= %{version}-%{release}
Provides: python-SOAPpy = %{version}-%{release}

%description
The goal of the SOAPpy team is to provide a full-featured SOAP library
for Python that is very simple to use and that fully supports dynamic
interaction between clients and servers.

%prep
%setup -n %{real_name}-%{version}

### Remove shell bangs
for file in $(find SOAPpy/wstools/ -type f -name \*.py); do
    %{__cp} $file $file.orig
    grep -v "\#\! \/usr\/bin" $file.orig > $file
    %{__rm} -f $file.orig
done

### Remove executable flag from example scripts
%{__chmod} -x bid/* contrib/* docs/* tools/* validate/*

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README RELEASE_INFO TODO bid/ contrib/ docs/ tools/ validate/
%{python_sitelib}/SOAPpy/

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 0.11.6-1
- Initial package. (based on fedora)
