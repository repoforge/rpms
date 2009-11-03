# $Id$
# Authority: matthias

Summary: Manipulation tool for Macromedia Flash Video (FLV) files
Name: flvtool2
Version: 1.0.6
Release: 1%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://www.inlet-media.de/flvtool2
Source: http://rubyforge.org/frs/download.php/17497/flvtool2-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: ruby
BuildRequires: ruby
BuildArch: noarch

%description
FLVTool2 is a manipulation tool for Macromedia Flash Video (FLV) files.
FLVTool2 can calculate a lot of meta data and insert a onMetaData tag. It can
cut FLV files and add cue Points (onCuePoint). A debug command lets you see
inside our FLV and the print command gives you meta data information in XML
or YAML format.


%prep
%setup


%build
ruby setup.rb config
ruby setup.rb setup


%install
%{__rm} -rf %{buildroot}
ruby setup.rb install --prefix=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README examples/
%{_bindir}/flvtool2
%{_prefix}/lib/ruby/site_ruby/*/flv.rb
%{_prefix}/lib/ruby/site_ruby/*/flvtool2.rb
%{_prefix}/lib/ruby/site_ruby/*/mixml.rb
%{_prefix}/lib/ruby/site_ruby/*/miyaml.rb
%{_prefix}/lib/ruby/site_ruby/*/flv/
%{_prefix}/lib/ruby/site_ruby/*/flvtool2/


%changelog
* Wed Feb 14 2007 Matthias Saou <http://freshrpms.net/> 1.0.6-1
- Update to 1.0.6 (final).

* Wed Feb  7 2007 Matthias Saou <http://freshrpms.net/> 1.0.5-0.1.rc6
- Initial RPM release.

