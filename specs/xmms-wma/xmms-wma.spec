# $Id$

%define xmms_inputdir %(xmms-config --input-plugin-dir)

Summary: X MultiMedia System input plugin to play Windows Media Audio files
Name: xmms-wma
Version: 1.0.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://mcmcc.bat.ru/xmms-wma/
Source: http://mcmcc.bat.ru/xmms-wma/xmms-wma-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.1, glib >= 1.2.7, gtk+ >= 1.2.7
BuildRequires: xmms-devel, gtk+-devel

%description
X MultiMedia System input plugin to play Windows Media Audio, aka WMA files.
This plug-in is written using the ffmpeg library (http://ffmpeg.sf.net)
written by Fabrice Bellard (to be exact, strongly advanced library).
Everything besides wma format support was removed from it to make it lighter.
Tag informations are converted from unicode to your system locale.


%prep
%setup


%build
OPTFLAGS="%{optflags}" %{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 libwma.so %{buildroot}%{xmms_inputdir}/libwma.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%lang(ru) %doc readme.rus
%doc readme.eng COPYING
%{xmms_inputdir}/libwma.so


%changelog
* Mon Jun  7 2004 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Initial rpm package.

