#
# spec file for package rubygem-yast-rake
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           rubygem-yast-rake
Version:        0.2.4
Release:        0
%define mod_name yast-rake
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://github.org/openSUSE/yast-rake
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Rake tasks providing basic work-flow for Yast development
License:        LGPL-2.1
Group:          Development/Languages/Ruby

%description
Rake tasks that support work-flow of Yast developer. It allows packaging repo,
send it to build service, create submit request to target repo or run client
from git repo.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING" \
  -f

%gem_packages

%changelog
