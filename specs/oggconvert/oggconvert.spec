# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define desktop_vendor rpmforge

Summary: Graphical tool to convert media to Free formats
Name: oggconvert
Version: 0.3.2
Release: 1%{?dist}
Group: Applications/Multimedia
License: LGPL
URL: http://oggconvert.tristanb.net/

Source: http://oggconvert.tristanb.net/releases/%{version}/oggconvert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: gstreamer
BuildRequires: gstreamer-python
BuildRequires: gstreamer-plugins-base
BuildRequires: gettext
BuildRequires: python-devel
BuildRequires: pygtk2 >= 2.10
BuildRequires: pygtk2-libglade >= 2.10
Requires: gstreamer
Requires: gstreamer-python
Requires: gstreamer-plugins-base
Requires: pygtk2 >= 2.10
Requires: pygtk2-libglade >= 2.10

%description
OggConvert is a small, open source utility for converting audio and video
files into the Vorbis audio format, and the Theora and Dirac video formats.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING PKG-INFO README TODO
%{_bindir}/oggconvert
%{_datadir}/applications/oggconvert.desktop
%{_datadir}/pixmaps/oggconvert.svg
%{python_sitelib}/OggConvert/

%changelog
* Thu Sep 18 2008 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Initial package. (using DAR)
