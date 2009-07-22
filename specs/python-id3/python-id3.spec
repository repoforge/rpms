# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name id3-py

Summary: ID3 tag library for Python
Name: python-id3
Version: 1.2
Release: 1
License: GPL
Group: Development/Libraries
URL: http://id3-py.sourceforge.net/

Source: http://dl.sf.net/id3-py/id3-py_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python
Provides: id3-py = %{version}-%{release}
Obsoletes: id3-py <= %{version}-%{release}

%description
This is a simple Python module for retrieving and setting so-called
ID3 tags on audio files through an object-oriented interface.  Players
generally use this simple information for display track title, artist
name, and album title while playing the sound file.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{python_sitelib}/ID3.py*
%{python_sitelib}/ID3.pyc
%ghost %{python_sitelib}/ID3.pyo

%changelog
* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
